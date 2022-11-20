from django.db import models
from Apps.Usuarios.models import Persona
from Apps.Sistema.models import Direccion
# Create your models here.




class Tipo(models.Model):
    nombre = models.CharField('Deporte', max_length=255, blank=True)
    emoji = models.CharField('Emoji', max_length=255, blank=True)
    def __str__(self):
        return '{} {}'.format(self.emoji,self.nombre)


class Marca(models.Model):
    nombre = models.CharField('Marca', max_length=255, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)


class CategoriaMaquinas(models.Model):
    nombre = models.CharField('Nombre', max_length=255, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)


class CategoriaAccesorios(models.Model):
    nombre = models.CharField('Nombre', max_length=255, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)



PRECIO_OPC = (
    (0,'Por horas'),
    (1,'Por hectarea'),
)

COMBUSTIBLE_OPC = (
    (0,'Yo'),
    (1,'Quien arrienda'),
    (2,'A tratar'),
)



class GaleriaFotos(models.Model):
    imagen1      = models.ImageField('Imagen', upload_to='maquinas', default='maquinas/1.png')
    imagen2      = models.ImageField('Imagen', upload_to='maquinas', default='maquinas/2.png')
    imagen3      = models.ImageField('Imagen', upload_to='maquinas', default='maquinas/3.png')
    imagen4      = models.ImageField('Imagen', upload_to='maquinas', default='maquinas/4.png')
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(str(self.date))

class Maquina(models.Model):
    t = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    cat = models.ForeignKey(CategoriaMaquinas, on_delete=models.SET_NULL, null=True, blank=True)
    m = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    mm = models.CharField('Modelo', max_length=255, blank=True)
    a = models.PositiveIntegerField('Año', default=2000, null=True, blank=True)
    pr = models.PositiveSmallIntegerField('Forma de cobro', choices=PRECIO_OPC, default=0)
    pre = models.IntegerField('Precio')
    c = models.PositiveSmallIntegerField('Quien paga el combustible?', choices=COMBUSTIBLE_OPC, default=0)
    f = models.OneToOneField(GaleriaFotos, on_delete=models.SET_NULL, null=True, blank=True)
    p = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    d = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.m)


class Tractor(models.Model):
    t = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    m = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    mm = models.CharField('Modelo', max_length=255, blank=True)
    a = models.PositiveIntegerField('Año', default=2000, null=True, blank=True)
    pr = models.PositiveSmallIntegerField('Forma de cobro', choices=PRECIO_OPC, default=0)
    pre = models.IntegerField('Precio')
    c = models.PositiveSmallIntegerField('Quien paga el combustible?', choices=COMBUSTIBLE_OPC, default=0)
    f = models.OneToOneField(GaleriaFotos, on_delete=models.SET_NULL, null=True, blank=True)
    p = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    d = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.m)
    

class Accesorio(models.Model):
    nombre = models.CharField('Nombre máquina', max_length=255, blank=True)
    t = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    cat = models.ForeignKey(CategoriaAccesorios, on_delete=models.SET_NULL, null=True, blank=True)
    pr = models.PositiveSmallIntegerField('Forma de cobro', choices=PRECIO_OPC, default=0)
    pre = models.IntegerField('Precio')
    f = models.OneToOneField(GaleriaFotos, on_delete=models.SET_NULL, null=True, blank=True)
    p = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)
    d = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    
    
