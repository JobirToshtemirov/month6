# Generated by Django 5.1.1 on 2024-09-19 19:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField(auto_now_add=True, verbose_name='Дата зачисления')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='Студент')),
            ],
        ),
    ]
