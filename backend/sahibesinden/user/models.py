from django.db import models

class GeneralUser(models.Model):
    #METHODS
    def signUp(self):
        pass
    def logIn(self):
        pass
    def searchAndFilter(self):
        pass
    def showAd(self):
        pass

class Member(GeneralUser):
    #FİELDS
    userName = models.CharField(max_length=100)
    userEmail = models.EmailFieldField(unique=True)
    userPassword = models.CharField(max_length=100)
    messagingHistory = models.TextField(blank=True) #not a real stack just for representative
    buyingHistory = models.TextField(blank=True) #not a real stack just for representative
    likedAds = models.ManyToManyField('ads.Ad', blank=True, related_name='liked_by')
    rating = models.FloatField(default=0.0)
    telNumber = models.FloatField()

    #METHODS
    def addingAd(self):
        pass
    def updateAd(self):
        pass
    def payment(self):
        pass
    def message(self):
        pass
    def editProfile(self):
        pass
    def __str__(self):
        return self.userName
    
class Admin(Member):
    #FİELDS
    name = models.CharField(max_length=100)

    #METHODS
    def deleteMember(self):
        pass
    def deleteAd(self):
        pass

    def __str__(self):
        return self.name













# Create your models here.
