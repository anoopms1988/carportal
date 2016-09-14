from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


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


class EmailConfirmation(models.Model):
    user = models.OneToOneField(User, related_name='email_confirmation', on_delete=models.CASCADE, unique=True)
    email_verfied = models.BooleanField(default=False, null=False, blank=False)
    token = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(null=False, blank=False)

    class Meta:
        verbose_name = _("Email Confirmation")
        verbose_name_plural = _("Email Confirmation")

class LoginAttempts(models.Model):
    class Meta:
        db_table = 'login_failed_attempts'

    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    failed_time = models.DateTimeField(auto_now=True, null=True)
    ip_address = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=255, null=True)