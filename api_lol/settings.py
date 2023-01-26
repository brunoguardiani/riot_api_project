"""
Django settings for api_lol project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from enum import Enum
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from .cors_config import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iwgc32gh0$_fdqe&6cu3ojlcd+co=+*7a^h3mk=m9vn0o!0zlb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  '*'
]

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
  'django.contrib.sessions', 'django.contrib.messages',
  'django.contrib.staticfiles', 'rest_framework', 'corsheaders'
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_lol.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

WSGI_APPLICATION = 'api_lol.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = ['Content-Type']
CORS_ALLOW_METHODS = [
  'DELETE',
  'GET',
  'OPTIONS',
  'PATCH',
  'POST',
  'PUT',
]

CORS_ALLOW_CREDENTIALS = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

API_KEY = 'RGAPI-31260d13-730e-43f7-af58-467eb963ad71'

API_URL = 'https://br1.api.riotgames.com/lol'

DDRAGON_VERSION = '13.1.1'

class RIOT_API_URLS(Enum):
  TIER_IMAGES_URL = 'https://github.com/InFinity54/LoL_DDragon/tree/master/extras/tier'
  SUMMONER_V4_URL = f'{API_URL}/summoner/v4/summoners'
  CHAMPIONS_MASTERIES = f'{API_URL}/champion-mastery/v4/champion-masteries/by-summoner'
  DDRAGON_DATASET = f'http://ddragon.leagueoflegends.com/cdn/{DDRAGON_VERSION}'
  LEAGUE_V4_URL = f'{API_URL}/league/v4'
