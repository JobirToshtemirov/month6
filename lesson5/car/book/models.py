from django.db import models

# Create your models here.
from django.db import models


class BooksModel(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    count = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

