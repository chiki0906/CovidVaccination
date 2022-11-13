from django.db import models

# Create your models here.

class Vaccination(models.Model):
    center_name= models.CharField(max_length=100)
    place= models.CharField(max_length=200)
    available= models.IntegerField(default=10)
