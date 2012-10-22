
import os

path = lambda *s: os.path.join(os.path.dirname(os.path.abspath(__file__)), *s)

DEBUG = False
SITE_ID = 1
STATIC_URL = '/static/'
ROOT_URLCONF = 'damm.urls'
TEMPLATE_DIRS = (path("templates"),)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path('dev.db'),
    }
}

INSTALLED_APPS = (
    'damm.blog',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

try:
    from local_settings import *
except ImportError:
    pass

TEMPLATE_DEBUG = DEBUG
