from __future__ import unicode_literals

from django.db import models


# Create your models here.
class FakeData(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    age = models.IntegerField()
    date = models.DateField()
    timestamp = models.DateTimeField()

    def as_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'age': self.age,
            'date': str(self.date),
            'timestamp': str(self.timestamp)
        }
