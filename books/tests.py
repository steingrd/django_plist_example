
from django.test import TestCase

class BooksViewTest(TestCase):
    
    fixtures = ("testdata",)
    urls = "books.urls"
    
    def test_root_renders_index_template(self):
        response = self.client.get("/")
        self.assertContains(response, "books example")
        
    def test_all_authors_uses_render_array_shortcut(self):
        response = self.client.get("/all_authors/")
        self.assertContains(response, "<key>name</key><string>James Bennett</string>")
        
    def test_single_author_uses_render_dict_shortcut(self):
        response = self.client.get("/single_author/1/")
        self.assertContains(response, "<key>name</key><string>James Bennett</string>")
        
    def test_all_books_uses_array_generic_view(self):
        response = self.client.get("/all_books/")
        self.assertContains(response, "<key>title</key><string>Pro Django</string>")
        
    def test_single_book_uses_dict_generic_view(self):
        response = self.client.get("/single_book/1/")
        self.assertContains(response, "<string>Django 1.0 Website Development</string>")