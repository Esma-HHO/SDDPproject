from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Member(AbstractUser):
    email = models.EmailField(unique=True)
    messagingHistory = models.TextField(blank=True)
    buyingHistory = models.TextField(blank=True)
    rating = models.FloatField(default=0)
    telNumber = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    # Çakışmayı önlemek için related_name ekliyoruz:
    groups = models.ManyToManyField(
        Group,
        related_name="user_member_set",  # orijinalden farklı bir isim
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_member_set",  # orijinalden farklı bir isim
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username
