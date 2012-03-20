# Django settings for pyvec project.

import os,pyvec

PROJECT_ROOT = os.path.abspath(os.path.dirname(pyvec.__file__))
p = lambda x: os.path.join(PROJECT_ROOT, x)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = p(os.path.join('db','development.sqlite'))             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = p('static')
MEDIA_URL = '/media/'
STATIC_ROOT = p('staticc')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    p('static'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LANGUAGE_CODE="cs"


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'libj)6k5r^$+8b(if01l#!#=can9!t73#sd-m8!_5=7rydx#a3'

NEWMAN_MEDIA_PREFIX = MEDIA_URL + 'newman/'

NEWMAN_MEDIA_PREFIX = '/%s/newman/' % STATIC_URL.strip('/')

DEFAULT_MARKUP = 'markdown'

CACHE_BACKEND = 'dummy://'
