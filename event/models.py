from django.db import models

# Create your models here.
class Event(models.Model):
    eventId = models.CharField(max_length=200)