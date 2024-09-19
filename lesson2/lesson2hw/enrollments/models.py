from django.db import models

# Create your models here.
from django.db import models
from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Дата зачисления")

    def __str__(self):
        return f'{self.student.user.get_full_name()} зачислен на {self.course.title}'
