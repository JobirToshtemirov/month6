from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, verbose_name="Номер студенческого билета")
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return self.user.get_full_name()
