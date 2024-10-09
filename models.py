# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class CustomUser(AbstractUser):
    # You can add additional fields here if needed
    pass

class RegistrationLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    success = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} registered on {self.timestamp}"

class LoginAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"Login attempt by {self.user.username if self.user else 'Unknown'} on {self.timestamp}"
