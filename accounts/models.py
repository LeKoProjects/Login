# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # outros campos personalizados, se houver
    
    # Adicionar related_name para evitar conflitos de acessores reversos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        help_text='Specific permissions for this user.',
        related_query_name='user'
    )