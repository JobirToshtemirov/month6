from django.db import models

# Create your models here.
from django.db import models
from courses.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название урока")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name="Курс")
    content = models.TextField(verbose_name="Содержание урока")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title
