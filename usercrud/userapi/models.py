from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    age = models.IntegerField(default=0)


