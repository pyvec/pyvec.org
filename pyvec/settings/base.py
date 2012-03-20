import os,pyvec

PROJECT_ROOT = os.path.abspath(os.path.dirname(pyvec.__file__))
p = lambda x: os.path.join(PROJECT_ROOT, x)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'pyvec.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    p('templates')
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.redirects',

    'ella.core',
    'ella.photos',
    'ella.articles',
    'ella.positions',

    'newman',

    'djangomarkup',
    'pyvec.core',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'ella.newman.context_processors.newman_media',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "newman.context_processors.newman_media",
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.contrib.messages.context_processors.messages",
	'django.core.context_processors.request',
)

CATEGORY_TEMPLATES = (
    ('category.html', 'default (category.html)'),
    ('staticp.html', 'static page (staticp.html)')
)