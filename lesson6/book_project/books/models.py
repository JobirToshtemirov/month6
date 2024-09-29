from django.db import models

# Create your models here.
from django.db import models


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title
