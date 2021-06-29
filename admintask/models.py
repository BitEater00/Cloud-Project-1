from django.db import models
from event.models import Event
from student.models import Student
from club.models import Club

# Create your models here.
class registration(models.Model):
    eventId = models.CharField(max_length=200)
    studentId = models.CharField(max_length=200)

class subscription(models.Model):
    clubId = models.CharField(max_length=200)
    studentId = models.CharField(max_length=200)