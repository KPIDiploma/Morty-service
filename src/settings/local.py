"""
Local settings. File must be named `local.py`.
In this file you must specify you credentials to db
and other variables like as DEBUG=True
"""

from .common import *


DATABASES['default'].update({
    'NAME': 'morty_db',
    'USER': 'morty',
    'PASSWORD': 'admin',
    'HOST': '127.0.0.1',
    'PORT': '25432',
})

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'kryvonis.artem@gmail.com'
EMAIL_HOST_PASSWORD = ''

SECRET_KEY = 'q*12333123afasvbotllblv44+7@q#xg(j#h8ggsa2g!*cfj9!o_kuyx8fgwz%'
