from django.db import models

# Create your models here.
class Vehicle(models.Model):
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    note = brand = models.CharField(max_length=500)
    