# ads/models.py
from django.db import models
from user.models import Member
from django.conf import settings
from django.contrib.auth.models import User

# İlan interface'i (abstract model)
class Ad(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    comments = models.TextField(blank=True)
    bargaining = models.BooleanField(default=False)
    adDate = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    likedRate = models.FloatField(default=0)

    class Meta:
        abstract = True

# Alt sınıflar
class Car(Ad):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    productionYear = models.DateField()
    millage = models.FloatField()
    transmission = models.BooleanField()
    fuelType = models.CharField(max_length=50)
    liked_by = models.ManyToManyField(Member, related_name='likedCars', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars') 

class House(Ad):
    rooms = models.IntegerField()
    size_m2 = models.FloatField()
    floor = models.IntegerField()
    buildYear = models.IntegerField()
    liked_by = models.ManyToManyField(Member, related_name='likedHouses', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='houses') 

class Furniture(Ad):
    type = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    liked_by = models.ManyToManyField(Member, related_name='likedFurnitures', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='furnitures') 
