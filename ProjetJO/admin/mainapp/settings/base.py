"""
https://docs.djangoproject.com/fr/3.2/topics/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Pensez à générer une nouvelle clé à l'aide de https://djecrety.ir/
SECRET_KEY = "velicyjh0)jmde&@qj=_)hzik!&sw4ml8b92ni&!y@=cu(-hj8"


INSTALLED_APPS = [
    "corsheaders",
    'rest_framework',
    "mainapp.apps.MainappConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]



# Les URLs sont désormais déclarées dans leur propre module
ROOT_URLCONF = "mainapp.urls"

WSGI_APPLICATION = "mainapp.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/fr/3.2/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'api_JOTICKET',
    'USER': 'root', 
    'PASSWORD':'',
    'HOST': '127.0.0.1', 
    'PORT': '3306', 
    }
}

# Password validation
# https://docs.djangoproject.com/fr/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/fr/3.2/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/fr/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/fr/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# LOGIN_URL = 'connexion'
LOGIN_URL = 'connexion'

# GESTION DES AUTORISATIONS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'http://127.0.0.1:5500'
    "http://127.0.0.1:8000",
]
ALLOWED_HOSTS = [
    '127.0.0.1',
]
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
]
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5500",
]

SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False 
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False 
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')