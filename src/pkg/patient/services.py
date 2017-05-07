from django.contrib.auth import get_user_model

from src.pkg.patient.notifications.service import UserNotifications


class PatientService:
    # email_service = UserNotifications()

    @staticmethod
    def register(email, password, **extra_fields):
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        UserNotifications().send_password_to_user(user=user, password=password)

        return user
