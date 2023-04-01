"""
Django settings for hrm project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load enviroment variable
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ['localhost', '127.0.0.1', 'pythonanywhere.com']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']
X_FRAME_OPTIONS = 'ALLOW-FROM https://www.pythonanywhere.com'
# X_FRAME_OPTIONS = 'ALLOW-FROM http://127.0.0.1:8000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # new apps
    'src.dashboard.apps.DashboardConfig',
    'src.staff.apps.StaffConfig',
    'src.office.apps.OfficeConfig',
    'src.record.apps.RecordConfig',
    'src.recruitment.apps.RecruitmentConfig',
    'src.account.apps.AccountConfig',

    'api.apps.ApiConfig',

    "debug_toolbar",
    'rest_framework',
    'django_extensions',
    'django_cleanup.apps.CleanupConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'src.dashboard.settings_middleware.SettingsGuaranteeMiddleware',
]


AUTH_USER_MODEL = 'account.AccountUser'

ROOT_URLCONF = 'hrm.urls'
LOGOUT_REDIRECT_URL = '/login'
LOGIN_REDIRECT = '/'
LOGIN_URL = '/login'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR / 'frontend',
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'src.office.context_processors.departments',
            ],
        },
    },
]

WSGI_APPLICATION = 'hrm.wsgi.application'
ASGI_APPLICATION = 'hrm.asgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

''' :Use postgres backend only when database is setup. create .env file in the root directory 
    and include 
        - PG_DB_NAME = '<database_name>'
        - PG_DB_USER = '<database_user>'
        - PG_DB_PASSWORD = '<database_password>'
        - PG_DB_HOST = <defaults to localhost else provide 'host url'>
        - PG_DB_POST = <defaults to 5432 else provide port>
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',


        # POSTGRESSSQL
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.getenv('PG_DB_NAME'),
        # 'USER': os.getenv('PG_DB_USER'),
        # 'PASSWORD': os.getenv('PG_DB_PASSWORD'),
        # 'HOST': os.getenv('PG_DB_HOST'),
        # 'PORT': os.getenv('PG_DB_PORT'),
    }
}

'''
    :Cache backend - Uncomment below code to activate cache backend.
    :Options - Redis requires extra configurations like docker container running on specifies port.
'''

# Cache
# CACHES = {
#     'default': {
#         # REDIS CACHE
#         # 'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         # 'LOCATION': 'redis://127.0.0.1:6379',

#         # DatabaseCache
#         # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         # 'LOCATION': 'cache_base'
#     }
# }


# Whitenoise static files caching and comression
STORAGES = {
    # ...
    "staticfiles": {
        # "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'  # noqa: E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/files/'

MEDIA_ROOT = BASE_DIR / 'docs'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
