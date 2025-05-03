from django.db import models

class GeneralUser(models.Model):
    #METHODS
    pass

class Member(GeneralUser):
    #FİELDS
    userName = models.CharField(max_length=100)
    userEmail = models.EmailField(unique=True)
    userPassword = models.CharField(max_length=100)
    messagingHistory = models.TextField(blank=True) #not a real stack just for representative
    buyingHistory = models.TextField(blank=True) #not a real stack just for representative
    liked_cars = models.ManyToManyField('ads.Car', blank=True, related_name='liked_by_members')
    liked_houses = models.ManyToManyField('ads.House', blank=True, related_name='liked_by_members')
    liked_furniture = models.ManyToManyField('ads.Furniture', blank=True, related_name='liked_by_members')
    rating = models.FloatField(default=0.0)
    telNumber = models.FloatField()

    #METHODS
    def __str__(self):
        return self.userName
    
class Admin(Member):
    #FİELDS
    name = models.CharField(max_length=100)

    #METHODS
    def __str__(self):
        return self.name
