from django.db import models
from Apps.Usuarios.models import Persona
from Apps.Sistema.models import Direccion
# Create your models here.



class Tipo(models.Model):
    nombre = models.CharField('Deporte', max_length=255, blank=True)
    emoji = models.CharField('Emoji', max_length=255, blank=True)
    def __str__(self):
        return '{} {}'.format(self.emoji,self.nombre)

class Categoria(models.Model):
    nombre = models.CharField('Categoria', max_length=255, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)

class Clase(models.Model):
    nombre = models.CharField('Nombre de la clase', max_length=255, blank=True)
    cat = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)



class GaleriaFotos(models.Model):
    imagen1      = models.ImageField('Imagen', upload_to='canchas', default='canchas/1.png')
    imagen2      = models.ImageField('Imagen', upload_to='canchas', default='canchas/2.png')
    imagen3      = models.ImageField('Imagen', upload_to='canchas', default='canchas/3.png')
    imagen4      = models.ImageField('Imagen', upload_to='canchas', default='canchas/4.png')
    imagen5      = models.ImageField('Imagen', upload_to='canchas', default='canchas/5.png')
    imagen6      = models.ImageField('Imagen', upload_to='canchas', default='canchas/6.png')
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(str(self.date))

class Cancha(models.Model):
    nombre = models.CharField('Nombre de la cancha', max_length=255, blank=True)
    imagen      = models.ImageField('Logo', upload_to='canchas', default='canchas/default.png')
    cat = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    f = models.OneToOneField(GaleriaFotos, on_delete=models.SET_NULL, null=True, blank=True)
    p = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    d = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)

class Horario(models.Model):
    c = models.ForeignKey(Cancha, on_delete=models.SET_NULL, null=True, blank=True)
    d = models.DateField('Fecha')
    i = models.TimeField('Inicio bloque')
    t = models.TimeField('Término bloque')
    p = models.IntegerField('Precio del bloque')
    l = models.BooleanField('Ocupada?', default=False)
    def get_precio(self):
        import re
        return (re.sub(r'(?<!^)(?=(\d{3})+$)', r'.',str(self.p)))
    def __str__(self):
        return '{}'.format(self.c)


class Reserva(models.Model):
    h = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True, blank=True)
    p = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    pa = models.BooleanField('Pagado?', default=False)
    a = models.BooleanField('Aprobado?', default=False)
    def __str__(self):
        return '{} - {}/{}'.format(self.h.c.nombre, self.h.i, self.h.t)
