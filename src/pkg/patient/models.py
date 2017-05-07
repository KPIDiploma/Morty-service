from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext as _
from django.contrib.postgres.fields import ArrayField

from pkg.patient.choices import BloodTypeEnum, PatientStatus, SexEnum


class PatientManager(BaseUserManager):
    def _create_user(self, email, password, fullname,
                     **extra_fields):
        """
        Create and save a User with the given email and password.
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """

        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            fullname=fullname,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, fullname=None,
                    **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, fullname,
                                 **extra_fields)

    def create_superuser(self, email, password=None, fullname=None,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, fullname,
                                 **extra_fields)


class Doctor(models.Model):
    fullname = models.CharField(
        verbose_name=_('Full name'),
        max_length=300,
    )


class Patient(AbstractUser):
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=30,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=30,
        null=True,
        blank=True
    )

    fullname = models.CharField(
        verbose_name=_('Full name'),
        max_length=300,
    )

    birthday = models.DateField(
        verbose_name=_('date of the birth'),
        null=True,
        blank=True,
    )

    address = models.CharField(
        verbose_name=_('Address'),
        max_length=300,
        blank=True,
        null=True,
    )

    mobile = models.CharField(
        verbose_name=_('Mobile number'),
        max_length=13,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        verbose_name=_('E-mail'),
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        verbose_name=_('username'),
        max_length=100,
        null=True,
        blank=True,
    )

    sex = models.CharField(
        choices=SexEnum.choices(),
        max_length=6,
        null=True,
        blank=True,
    )

    blood_type = models.CharField(
        choices=BloodTypeEnum.choices(),
        max_length=3,
        null=True,
        blank=True,
    )

    status = models.IntegerField(
        choices=PatientStatus.choices(),
        null=True,
        blank=True,
    )

    doctors = models.ManyToManyField(Doctor)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    objects = PatientManager()

    @staticmethod
    def get_current_patients(author):
        patients = Patient.objects.get(email=author.email).patients.filter(
            status=PatientStatus.Hospital.value
        )

        return patients
