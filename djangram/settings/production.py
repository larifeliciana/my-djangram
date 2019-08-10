import django_heroku
from decouple import config

from djangram.settings.base import *

DEBUG = True



ALLOWED_HOSTS = [
    '.herokuapp.com',
]


# Dropbox for media files
#DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
#DROPBOX_OAUTH2_TOKEN = ''


django_heroku.settings(locals())
