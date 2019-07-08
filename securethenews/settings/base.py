"""
Django settings for securethenews project.

Generated by 'django-admin startproject' using Django 1.9.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',

    'sites',
    'pledges',
    'blog',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',

    'wagtailmenus',
    'webpack_loader',
    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'analytical',

    'django_filters',
    'crispy_forms',
    'rest_framework',
    'corsheaders',
    'django_logging'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'django_logging.middleware.DjangoLoggingMiddleware'
]

# Anyone can use the API via CORS
CORS_ORIGIN_ALLOW_ALL = True
# API is read-only
CORS_ALLOW_METHODS = ('GET', 'HEAD', 'OPTIONS')

ROOT_URLCONF = 'securethenews.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtailmenus.context_processors.wagtailmenus',
            ],
        },
    },
]

WSGI_APPLICATION = 'securethenews.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if 'DJANGO_DB_HOST' not in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'stn-build',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DJANGO_DB_NAME', 'stn'),
            'USER': os.environ['DJANGO_DB_USER'],
            'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
            'HOST': os.environ['DJANGO_DB_HOST'],
            'PORT': os.environ['DJANGO_DB_PORT']
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(BASE_DIR, 'client', 'build'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "securethenews"

# Base URL to use when referring to full URLs within the Wagtail -
# admin backend e.g. in notification emails. Don't include
# '/admin' or a trailing slash
BASE_URL = 'https://securethe.news'


# API framework settings, relevant only for /api
REST_FRAMEWORK = {
    # For any query, users can set both limit and offset.
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    # A page has 100 results by default, but there's no upper limit.
    'PAGE_SIZE': 100,
}

# Shiny forms for the web view of the API
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Django-webpack configuration
WEBPACK_LOADER = {  # noqa: W605
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': '/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR,
                                   'client/build/webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

# Django test xml output
#

if os.environ.get('DJANGO_XMLTEST_OUTPUT', 'no').lower() in ['yes', 'true']:
    TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
    TEST_OUTPUT_DIR = "/django-logs"
    TEST_OUTPUT_FILE_NAME = "app-tests.xml"
    TEST_OUTPUT_DESCRIPTIONS = True
    TEST_OUTPUT_VERBOSE = 2
