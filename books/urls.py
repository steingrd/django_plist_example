from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django_plist.views.generic import plist_array, plist_dict

from models import Author, Book
from views import all_authors, single_author

urlpatterns = patterns('',
    url('^$', direct_to_template, {'template': 'books/index.html'}),
    url('^all_books/$', plist_array, {'queryset': Book.objects.all()}),
    url('^single_book/(?P<object_id>\d+)/$', plist_dict, {'queryset': Book.objects.all()}),
    url('^all_authors/$', all_authors),
    url('^single_author/(?P<author_id>\d+)/$', single_author),
)
