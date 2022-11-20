from django.contrib import admin
from .models import Tipo,Maquina, Accesorio, Tractor, Marca, GaleriaFotos, CategoriaAccesorios, CategoriaMaquinas
# Register your models here.


admin.site.register(Tipo)
admin.site.register(Maquina)
admin.site.register(Accesorio)
admin.site.register(Tractor)
admin.site.register(Marca)
admin.site.register(GaleriaFotos)
admin.site.register(CategoriaAccesorios)
admin.site.register(CategoriaMaquinas)