from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^django_plist_example/', include('django_plist_example.foo.urls')),

    (r'^admin/(.*)', admin.site.root),
)
