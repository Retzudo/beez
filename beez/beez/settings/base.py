import datetime
import os

import dj_database_url
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.getenv('BEEZ_SECRET_KEY', os.urandom(24))

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('BEEZ_STATIC_ROOT', os.path.join(BASE_DIR, '../static'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

PRIVATE_STORAGE_ROOT  = os.getenv('BEEZ_PRIVATE_STORAGE_ROOT', os.path.join(BASE_DIR, '../media'))
PRIVATE_STORAGE_AUTH_FUNCTION = 'private_storage.permissions.allow_staff'

OWM_API_KEY = os.getenv('BEEZ_OWM_API_KEY')

LOGIN_REDIRECT_URL = reverse_lazy('frontend:apiary-list')

WSGI_APPLICATION = 'beez.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///'+os.path.abspath(os.path.join(BASE_DIR, 'db.sqlite3')))
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'markdown_deux',
    'qr_code',
    'core',
    'frontend',
    'api',
    'rest_framework',
    'rest_framework_jwt',
    'drf_yasg',
    'django_filters',
    'django.contrib.admin',
    'widget_tweaks',
    'private_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'beez.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'beez.version',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,  # Don't render lat/lon as string. We don't need the precision
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'jwt': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}