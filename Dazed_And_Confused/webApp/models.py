from datetime import date
from datetime import datetime
from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        unique_together = [('email', 'password')]
        ordering = ['email']
