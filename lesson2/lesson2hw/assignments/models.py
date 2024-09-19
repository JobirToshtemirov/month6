from django.db import models

# Create your models here.
from django.db import models
from lessons.models import Lesson

class Assignment(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название задания")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    due_date = models.DateField(verbose_name="Дата сдачи")
    description = models.TextField(verbose_name="Описание задания")

    def __str__(self):
        return self.title
