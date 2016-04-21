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


class FakeOutput(models.Model):
    time_stamp = models.DateField()
    module_name = models.CharField(max_length=50)  # temperature, humidity, short description
    output_value = models.FloatField()
    tag = models.CharField(max_length=50)

    def as_json(self):
        return {
            'module_name': self.module_name,
            'output_value': self.output_value,
            'tag': self.tag,
            'time_stamp': str(self.time_stamp)
        }


class FakeLog(models.Model):
    time_stamp = models.DateField()
    module_name = models.CharField(max_length=50)
    log_level = models.IntegerField()
    log_message = models.TextField()

    def as_json(self):
        return {
            'module_name': self.module_name,
            'log_level': self.log_level,
            'log_message': self.log_message,
            'time_stamp': str(self.time_stamp)
        }
