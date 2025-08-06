from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
