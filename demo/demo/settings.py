"""
Django settings for demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from os.path import normpath, join

from django import VERSION as DJANGO_VERSION

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = os.path.dirname(os.path.join(BASE_DIR, 'demo'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1g&e2*#444qj833xb2wr0%r0xj2$b_o_d_03nw&zkq%f=1xq(u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

""" TEMPLATE CONFIGURATION """

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.normpath(os.path.join(SITE_ROOT, 'templates')),
        ],
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',  # Required for django comment next url, allauth
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    },
]

########## END TEMPLATE CONFIGURATION

ALLOWED_HOSTS = []

""" APP CONFIGURATION """
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for comments and allauth
    'django.contrib.sitemaps',
)

THIRD_PARTY_APPS = (
    'authtools',  # Custom User classes
    'allauth',  # Login using email
    'allauth.account',
    'allauth.socialaccount',
    'andablog',  # The blog engine
    'django_extensions',  # Misc Tools, we use it for the handy sql reset
    'django_comments',  # Replacement for Django contrib comments
    'bootstrapform',  # Required for bootstrap templates
    'markitup',  # Blog req: For markdown editing
    "taggit",   # Blog req: For tags
)

THIRD_PARTY_APPS += ('debug_toolbar.apps.DebugToolbarConfig',)

# Apps specific for this project go here.
LOCAL_APPS = (
    'common',
    'profiles',
    'democomments',
    'blog',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # Needed to login by username in Django admin
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

""" MEDIA CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

""" STATIC FILE CONFIGURATION """
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
########## END STATIC FILE CONFIGURATION

""" CUSTOM USER CONFIGURATION """
AUTH_USER_MODEL = 'common.User'

""" All Auth """
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_DISPLAY = lambda user: user.get_short_name()
ACCOUNT_EMAIL_VERIFICATION = "optional"

# Django Auth
LOGIN_REDIRECT_URL = '/profile/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

""" Comments Configuration """
COMMENTS_APP = 'democomments'

""" Markitup! Settings """
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})
MARKITUP_SET = 'markitup/sets/markdown'