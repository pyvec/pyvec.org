from django.conf.urls.defaults import *
from django.conf import settings

from ella import newman

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# make sure to import ella error handlers
from ella.core.urls import handler404, handler500

# register ella's admin
newman.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pyvec/', include('pyvec.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # only use these urls in DEBUG mode, otherwise they should be handled by your web server
    from os.path import dirname, join, normpath

    import django, ella


    # static files from both admin apps
    ADMIN_ROOTS = (
        normpath(join(dirname(ella.__file__), 'newman', 'media')),
        normpath(join(dirname(django.__file__), 'contrib', 'admin', 'media')),
    )

    # serve static files
    urlpatterns += patterns('',
        # newman specific files first
        (r'^%s/(?P<path>.*)$' % settings.NEWMAN_MEDIA_PREFIX.strip('/'), 'ella.utils.views.fallback_serve', {'document_roots': ADMIN_ROOTS}),
        # rest of the static files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )


# actual URL mappings
urlpatterns += patterns('',
    (r'^newman/', include(newman.site.urls)),
    (r'^', include('ella.core.urls')),
#    (r'^',include('django.contrib.auth.urls')),
)
