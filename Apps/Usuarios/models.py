from django.db import models
from django.contrib.auth.models import AbstractUser



class Persona(AbstractUser):
    email       = models.EmailField('email address', unique=True)
    imagen      = models.ImageField('Foto de perfil', upload_to='perfiles', default='perfiles/default.png')
    telefono    = models.CharField('Teléfono', max_length=11, default='+56')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  


