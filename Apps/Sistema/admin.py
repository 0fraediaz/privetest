from django.contrib import admin

# Register your models here.
from .models import Comuna, Region, Direccion

admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Direccion)