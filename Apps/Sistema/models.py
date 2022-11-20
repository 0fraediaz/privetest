from django.db import models

# Create your models here.

class Region(models.Model):
    nombre      = models.CharField('Nombre' ,max_length=124)
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre      = models.CharField('Nombre' ,max_length=124)
    region      = models.ForeignKey(Region(), on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle       = models.CharField('Calle', max_length=124)
    numero      = models.SmallIntegerField('Número', blank=True, null=True)
    comuna      = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING, blank=True)
    def __str__(self):
       return '{} #{}, {}'.format(self.calle, self.numero, self.comuna)