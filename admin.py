from django.contrib import admin

# Register your models here.
# admin.py

from .models import RegistrationLog, LoginAttempt

admin.site.register(RegistrationLog)
admin.site.register(LoginAttempt)
