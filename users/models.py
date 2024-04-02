from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime, uuid
# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Group(Base):
    name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return str(self.name)

class User(AbstractUser, Base):
    date_of_birth = models.DateField(null=True)
    mobile = models.CharField(max_length=16, null=True)
    gender = models.CharField(max_length=1, default='U')
    address = models.CharField(max_length=256, null=True)
    groups = models.ManyToManyField(Group)

    def __str__(self) -> str:
        return str(self.username)
