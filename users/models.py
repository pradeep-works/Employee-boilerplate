from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime, uuid
# Create your models here.

class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    mobile = models.CharField(max_length=16, null=True)
    gender = models.CharField(max_length=1, default='U')
    address = models.CharField(max_length=256, null=True)

# class Dummy(models.Model):
#     username = models.CharField(max_length=64)
#     email = models.EmailField()
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_add=True)
#     date_of_birth = models.DateField(null=True)