from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django AbstractUser.
    Includes a 'role' field to differentiate between user types.
    """
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('citizen', 'Citizen'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='citizen', help_text='User role for access control')

    def __str__(self):
        return self.username
