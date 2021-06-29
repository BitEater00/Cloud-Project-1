from django.db import models

# Create your models here.
class Student(models.Model):
    studentId = models.CharField(max_length=200)