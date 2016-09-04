from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, unique=True)
    gender = models.CharField(default='male', choices=GENDER, max_length=10, null=True, blank=True)
    city = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = ("User Profile")
