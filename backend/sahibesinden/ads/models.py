from django.db import models
from user.models import Member

class Ad(models.Model):
    #FİELDS
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    comments = models.TextField(blank=True)
    barganing = models.BooleanField(default=False)
    adDate = models.DateField()
    location = models.CharField(max_length=100)
    likedRate = models.FloatField(default=0.0)

    class Meta:
        abstract = True #for making Ad class interface

class Car(Ad):
    #FİELDS
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    productionYear = models.DateField()
    millage = models.FloatField()
    transmission = models.BooleanField(default=True)
    fuelType = models.CharField(max_length=50)

class House(Ad):
    #FİELDS
    rooms = models.IntegerField()
    size_m2 = models.FloatField()
    floor = models.IntegerField()
    buildYear = models.IntegerField()

class Furniture(Ad):
    #FİELDS
    type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)        



# Create your models here.
