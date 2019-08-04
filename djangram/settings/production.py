import django_heroku
from decouple import config

from djangram.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.herokuapp.com',
]

# Dropbox for media files
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = config('DROPBOX_OAUTH2_TOKEN', default='')

# Social auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', default='')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', default='')

# Email
#EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='projetosbcc2018@gmail.com')
#	EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='@123minha123')


django_heroku.settings(locals())
