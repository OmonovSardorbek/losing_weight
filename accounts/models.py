from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Role(models.Choices):
    ADMIN = 'Admin'
    CLIENT = 'Client'


class APPUser(AbstractUser):
    role = models.CharField(max_length=15, choices=Role.choices, default=Role.CLIENT)
