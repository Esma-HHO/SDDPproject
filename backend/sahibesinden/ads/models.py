# ads/models.py
from django.db import models
from sahibesinden.user.models import Member
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


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
    def __str__(self):
        return f"{self.brand} {self.model}"
    

class House(Ad):
    rooms = models.IntegerField()
    size_m2 = models.FloatField()
    floor = models.IntegerField()
    buildYear = models.IntegerField()
    liked_by = models.ManyToManyField(Member, related_name='likedHouses', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='houses')
    def __str__(self):
        return f"{self.location} {self.name}" 

class Furniture(Ad):
    type = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    liked_by = models.ManyToManyField(Member, related_name='likedFurnitures', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='furnitures') 
    def __str__(self):
        return f"{self.type} {self.name}"


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    listing = GenericForeignKey('content_type', 'object_id')
