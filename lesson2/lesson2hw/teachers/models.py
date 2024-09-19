from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="О преподавателе")
    department = models.CharField(max_length=100, verbose_name="Кафедра")

    def __str__(self):
        return self.user.get_full_name()
