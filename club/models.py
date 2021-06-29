from django.db import models

# Create your models here.
class Club(models.Model):
    clubId = models.CharField(max_length=200)