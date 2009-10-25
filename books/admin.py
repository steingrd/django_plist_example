
from django.contrib.admin import site, ModelAdmin

from models import Author
from models import Book
 
class AuthorAdmin(ModelAdmin):
    pass
 
class BookAdmin(ModelAdmin):
    pass

site.register(Author, AuthorAdmin)
site.register(Book, BookAdmin)

