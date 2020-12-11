from django.db import models

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.CharField(max_length = 64)
