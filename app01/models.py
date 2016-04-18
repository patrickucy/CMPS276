from __future__ import unicode_literals

from django.db import models


# Create your models here.
class FakeData(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    age = models.IntegerField()
