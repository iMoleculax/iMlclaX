"""
Projeto...: iMoleculaX -
Author....: Macedo, Glener Diniz - Engenheiro de Software Full Stack
dt-Incial.: 29 de Dezembro de 2025 - Última Alteração: 29 de Dezembro de 2025
"""
import os
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv('DEBUG', 1)))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web'

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'  # pasta destino do collectstatic

STATICFILES_DIRS = [
    BASE_DIR / 'templates' / 'static',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

MEDIA_URL = '/media/'
# /data/web/media
MEDIA_ROOT = DATA_DIR / 'media'

# Se não estiver com usuário logado, direciona para a url abaixo:
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/dashboard/'   # para onde o usuário vai depois de logar
LOGOUT_REDIRECT_URL = '/usuarios/login/'  # para onde vai depois de deslogar


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3%w!c@sh915p%g!sg1_rw9-hv(_96q_ci)ctrc7$@p7u7h()9k'


ALLOWED_HOSTS = [
    h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',')
    if h.strip()
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'projetos',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Local que define publica as variáveis o perfil do usuário que esta logado.
                'usuarios.context_processors.perfil_usuario',
                'usuarios.context_processors.uf_estados',

            ],
        },
    },
]


WSGI_APPLICATION = '_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# Banco de dados pro Defalt do Django
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'change-me'),
        'NAME': os.getenv('POSTGRES_DB', 'change-me'),
        'USER': os.getenv('POSTGRES_USER', 'change-me'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'change-me'),
        'HOST': os.getenv('POSTGRES_HOST', 'change-me'),
        'PORT': os.getenv('POSTGRES_PORT', 'change-me'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
