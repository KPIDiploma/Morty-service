from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext as _


class PatientManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
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
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, first_name, last_name, password, **extra_fields)


class Patient(AbstractUser):
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=30,
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=30,
    )
    birthday = models.DateField(
        verbose_name=_('date of the birth'),
        null=True,
        blank=True,
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = PatientManager()
