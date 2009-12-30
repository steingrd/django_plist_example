from django.shortcuts import get_object_or_404
from django_plist import render_array, render_dictionary
from models import Author

def all_authors(request):
    return render_array(Author.objects.all())


def single_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render_dictionary(author)