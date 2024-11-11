from django.db import models

# Create your models here.
class Food(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    age = models.IntegerField()