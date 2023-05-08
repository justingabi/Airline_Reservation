from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you want, e.g.
    # bio = models.TextField(max_length=500, blank=True)

    def str(self):
        return self.username

# Create your models here.
