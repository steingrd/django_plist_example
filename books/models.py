from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)
    nationality = models.CharField(max_length=2)

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author)
    price = models.IntegerField()
    released = models.DateField()
