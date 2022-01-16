from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100, blank=True)
    publishedDate = models.CharField(max_length=20, blank=True)
    ISBN = models.CharField(max_length=20, blank=True)
    pageCount = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(blank=True)
    language = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title
