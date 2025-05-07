from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    email = models.EmailField(unique=True)
    messagingHistory = models.TextField(blank=True)
    buyingHistory = models.TextField(blank=True)
    rating = models.FloatField(default=0)
    telNumber = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
