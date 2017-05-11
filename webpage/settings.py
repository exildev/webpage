#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for webpage project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$6tgkn!ug50hss(7z(vix!7&!r9rhz&mb*s2)e$(d2vtfxk9sg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'exile_ui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exile',
    'supra',
    'ace_overlay'
]

EXILE_UI = {
    'site_title': 'Exile web',
    'site_header': 'Exile web',
    'index_title': 'Gestor de contenido de Exile',
    'media': {
        'logo': {
            'dashboard': '/media/EXILE-small.png',
            'page': '/media/exile-72x72.png',
            'login': '/media/EXILE-small.png'
        },
        'icons':{
            'exile': {
                'icon': 'public',
                'groups': [
                    'Contenido', 'Configuracion', 'Principal', 'Contacto',
                ],
                'models': {
                    'Page': {'icon': 'language', 'group': 'Contenido'},
                    'Seccion': {'icon': 'grid_on', 'group': 'Contenido'},
                    'Item': {'icon': 'view_carousel', 'group': 'Contenido'},
                    'SubItem': {'icon': 'widgets', 'group': 'Contenido'},
                    'ItemSeccion': {'icon': 'settings', 'group': 'Configuracion' },
                    'SeccionFooter': {'icon': 'build', 'group': 'Contenido'},
                    'Menu': {'icon': 'menu', 'group': 'Contenido'},
                    'MenuPrincipal': {'icon': 'grade', 'group': 'Principal'},
                    'PaginaPrincipal': {'icon': 'grade', 'group': 'Principal'},
                    'FooterPrincipal': {'icon': 'grade', 'group': 'Principal'},
                    'Contacto': {'icon': 'person', 'group': 'Contacto'},
                    'Footer': {'icon': 'extension', 'group': 'Contenido'},
                },
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
        'name': 'exile',
        'models': [
            'Page',
            'Seccion',
            'Item',
            'SubItem',
            'Menu',
            'Footer'
        ]
    },

    {
        'name': 'auth',
        'models': [
            'Group',
            'User'
        ]
    },
    {
        'name': 'logout'
    }
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

ROOT_URLCONF = 'webpage.urls'

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

WSGI_APPLICATION = 'webpage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webpage',
        'USER': 'postgres',
        'PASSWORD': 'Exile*74522547',
        'HOST': '104.236.33.228',
        'POST': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Email configuration

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mariobarrios@exile.com.co'
EMAIL_HOST_PASSWORD = 'rrljhuvayivgzmms'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
