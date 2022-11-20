from django.urls import path
from .views import *


urlpatterns = [
   
    path('', InicioView, name='Inicio'),
    path('canchas', CanchasView),
    path('canchas/<id>', CanchaView),
    path('canchas/calendario/<id>', CanchaCalendarioView),
    path('canchas/bloque/<id>', BloqueView),
    path('deportes', DeportesView),
    
]
