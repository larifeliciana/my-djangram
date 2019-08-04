import django_heroku
from decouple import config

from djangram.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.herokuapp.com',
]


django_heroku.settings(locals())
