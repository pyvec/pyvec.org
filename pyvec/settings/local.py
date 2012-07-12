"""
Set variables from config.py that you want to override for local machine.
"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pyvec',
        'USER': 'root',
        'PASSWORD': 'root',
    },
}
