"""
Local settings. File must be named `local.py`.
In this file you must specify you credentials to db
and other variables like as DEBUG=True
"""

from .common import *


DATABASES['default'].update({
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '127.0.0.1',
    'PORT': '5432',
})

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

SECRET_KEY = ''
