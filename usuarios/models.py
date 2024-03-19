from django.db import models
from django.contrib.auth.models import AbstractUser    

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, verbose_name='Teléfono')    
    street = models.CharField(max_length=255, verbose_name='Calle')
    number = models.CharField(max_length=10, verbose_name='Número')
    zone = models.CharField(max_length=255, verbose_name='Reparto')
    category = models.CharField(max_length=255, verbose_name='Categoría Científica', blank=True, null=True)
    
    