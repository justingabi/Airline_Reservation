from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    userId = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def str(self):
        return self.username

# Create your models here.
