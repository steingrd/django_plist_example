from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^books/', include('books.urls')),
    (r'^admin/(.*)', admin.site.root),
)
