from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)
    blog = models.URLField()

    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author)
    price = models.IntegerField()
    released = models.DateField()

    def __unicode__(self):
        return self.title