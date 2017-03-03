"""
Local settings. File must be named `local.py`.
In this file you must specify you credentials to db
and other variables like as DEBUG=True
"""

from .common import *


DATABASES['default'].update({
    'USER': 'morty',
    'PASSWORD': 'admin',
    'HOST': '127.0.0.1',
    'PORT': '25432',
})
