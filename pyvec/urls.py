from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# make sure to import ella error handlers
from ella.core.urls import handler404, handler500

# register ella's admin
admin.autodiscover()

# actual URL mappings
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    (r'^', include('ella.core.urls')),
) + staticfiles_urlpatterns()
