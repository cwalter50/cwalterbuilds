"""
Django settings for cwalterbuilds project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
# import django_heroku


## this is a comment on testusers

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-r*t6z2u@1z7_k3oo+h-mw()e=x48nq563i5pp0(m-m!@sxgsbc'
# SECRET_KEY = 'django-insecure-b49d5b7f-69ab-4fe4-872d-ff331e2cdfdd'

# SECURITY WARNING: don't run with debug turned on in production!
# When Debug is true static files load... When it is false static files dont load. 
# https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
# I need it to be false so that the error pages work. 
# It should be true to make the static pages work... 
DEBUG = False
# DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'https://cwalterbuilds.herokuapp.com/', 'https://cwalterbuilds.herokuapp.com', 'cwalterbuilds.herokuapp.com', 'cwalterbuilds.herokuapp.com/']


# Application definition

INSTALLED_APPS = [
    'myprojects',
    'polls',
    'ordersorter',
    'birthdaycountdown',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'cwalterbuilds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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



WSGI_APPLICATION = 'cwalterbuilds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': ‘<db_name>’,
#         'USER': '<db_username>',
#         'PASSWORD': '<password>',
#         'HOST': '<db_host>',
#         'PORT': '<db_port>',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# AUTH_USER_MODEL = 'ordersorter.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


# if DEBUG:
#     MEDIA_URL = '/media/'
#     STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static','static-only')
#     MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static','media')
#     STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static'),)

# PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # STATIC_URL = '/static/'
# STATIC_ROOT = PROJECT_DIR + '/static/'



# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# this was added because i needed to run python3 manage.py collectstatic with every change to css file. It was very annoying.
# this should fix the problem so that I do not need to make that call with each change.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
#     'static/',
# )


# remove STATIC_ROOT


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Added for Authentications...
# This will change the default page after we login to whatever we define....
LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/'

# This will change the default page after we logout to whatever we define....
LOGOUT_REDIRECT_URL = ""


# Note: The password reset system requires that your website supports email, which is beyond the scope of this article, so this part won't work yet. To allow testing, put the following line at the end of your settings.py file. This logs any emails sent to the console (so you can copy the password reset link from the console).
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Activate Django-Heroku.
import django_heroku
django_heroku.settings(locals())
