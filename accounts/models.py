from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username
