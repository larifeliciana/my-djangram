import django_heroku
from decouple import config

from djangram.settings.base import *

DEBUG = False



ALLOWED_HOSTS = [
    '.herokuapp.com',
]


# Dropbox for media files
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DROPBOX_OAUTH2_TOKEN = 'em1Xkx6FqgAAAAAAAAAAD1mfWL7HgT_gcaK55k8HU_qpO0ueC_5GKk3lNVktM3zs'


django_heroku.settings(locals())
