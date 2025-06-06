import locale
from pathlib import Path
import environ
import os
from redis import Redis

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@mu6xuz_xuo%*^v77b9@^ci%(p2n=g0l6*-4^2fh-z&-h69tpd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jalali',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',
    'registerAPI',
    'jalali_date',
    'drf_yasg',
    'corsheaders',
    'users',
    'coreAPI',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

LANGUAGE_CODE = 'fa'

# default settings (optional)
JALALI_DATE_DEFAULTS = {
    # if change it to true then all dates of the list_display will convert to the Jalali.
    'LIST_DISPLAY_AUTO_CONVERT': False,
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali..js',

            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'moshavereAPI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }, ]

WSGI_APPLICATION = 'moshavereAPI.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DB_HOST = env("DB_HOST")
DB_NAME = env("DB_NAME")
DB_USERNAME = env("DB_USERNAME")
DB_PASSWORD = env("DB_PASSWORD")
DB_PORT = env("DB_PORT")
BOT_TOKEN = env("BOT_TOKEN")
CHAT_ID = env("CHAT_ID")
# PROXY_TYPE = env("PROXY_TYPE")
REQUEST_TIME_OUT = env("REQUEST_TIME_OUT", cast=float)
DOMAIN = env("DOMAIN")
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
REDIS_USERNAME = env("REDIS_USERNAME")
REDIS_PASSWORD = env("REDIS_PASSWORD")

# if PROXY_TYPE == 'socks5':
#     REQUEST_PROXY = {
#         "socks5": env("SOCKS_PROXY"),
#     }
#     PROXY_URL = env("SOCKS_PROXY")
# elif PROXY_TYPE == 'http':
#     REQUEST_PROXY = {
#         "http": env("HTTP_PROXY"),
#         "https": env("HTTP_PROXY"),
#     }
#     PROXY_URL = env("HTTP_PROXY")
# else:
#     REQUEST_PROXY = {
#         PROXY_TYPE: env("HTTPS_PROXY"),
#     }
#     PROXY_URL = env("HTTPS_PROXY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT
    }
}
redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, username=REDIS_USERNAME, password=REDIS_PASSWORD)
MELI_PAYAMAK_USERNAME = env("MELI_PAYAMAK_USERNAME")
MELI_PAYAMAK_PASSWORD = env("MELI_PAYAMAK_PASSWORD")
MELI_PAYAMAK_MESSAGE = env("MELI_PAYAMAK_MESSAGE")
MELI_PAYAMAK_PATTERN_NUMBER = env("MELI_PAYAMAK_PATTERN_NUMBER")
NOT_SEND_SMS_TIME_START = int(env("NOT_SEND_SMS_TIME_START"))
NOT_SEND_SMS_TIME_END = int(env("NOT_SEND_SMS_TIME_END"))