from django.db import models
from django.db import models


# Author jadvali
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book jadvali
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)  # Many-to-Many bog'lanish

    def __str__(self):
        return self.title


# Comment jadvali
class Comment(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # One-to-Many bog'lanish

    def __str__(self):
        return self.content
