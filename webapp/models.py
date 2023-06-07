from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=8)
    password = models.CharField(max_length=6)
    age = models.CharField(max_length=2)