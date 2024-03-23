from typing import Iterable
from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(Base):

    # id = models.BigIntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=32, db_index=True)
    id_number = models.IntegerField(unique=True, null=False, db_index=True)
    date_of_joining = models.DateField()
    salary = models.FloatField(null=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table_comment = 'This contains Employee data'
