from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site

from src.pkg.patient.notifications.service import UserNotifications
from src.pkg.patient.models import Patient
from src.pkg.common.permissions import MyTokenPermission


class PatientService:
    # email_service = UserNotifications()

    @staticmethod
    def register(password, **extra_fields):
        user = get_user_model().objects.create_user(
            password=password,
            **extra_fields
        )
        if not settings.DEBUG:
            UserNotifications().send_password_to_user(user=user,
                                                      password=password)

        return user

    @staticmethod
    def try_connect_doctor(doctor, patient, **kwargs):
        token = default_token_generator.make_token(patient)
        created, doctor_token = MyTokenPermission().create_token(doctor.id)
        if not created:
            return
        link = settings.CONNECT_TOKEN.format(
            doctor=doctor_token,
            token=token
        )
        link = '{}/{}'.format(Site.objects.get_current().domain, link)
        UserNotifications().send_doctor_connection(patient, link,
                                                   doctor.fullname)

    @staticmethod
    def final_connect_doctor(user, doctor_token, token):
        if default_token_generator.check_token(user, token):
            checked, doctor_id = MyTokenPermission().check_token(doctor_token)
            if not checked:
                return False

            patient = Patient.objects.get(pk=user.id)
            patient.doctors.add(doctor_id)
            patient.save()
        else:
            return False
