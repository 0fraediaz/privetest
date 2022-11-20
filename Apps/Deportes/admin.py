from django.contrib import admin
from .models import Tipo, Cancha , Clase, Categoria, Horario, Reserva, GaleriaFotos
# Register your models here.
admin.site.register(Tipo)
admin.site.register(Clase)
admin.site.register(Cancha)
admin.site.register(Categoria)
admin.site.register(Horario)
admin.site.register(Reserva)
admin.site.register(GaleriaFotos)