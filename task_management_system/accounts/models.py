from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)