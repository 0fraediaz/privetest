from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from poli_holas import azar
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate, login
from Apps.Deportes.models import Cancha, Horario


@login_required(login_url='login')
def InicioView(request):
    saludo1 = '👋 '
    saludo2 = ''
    a = azar()
    for x in a:
        saludo1 += str(x)
        saludo2= 'Ahora sabes saludar en '+str(a[str(x)])
    data = {
        'saludo1':saludo1,
        'saludo2':saludo2,
        'm1':'active',
    }
    return render(request, 'inicio.html', data)



@login_required(login_url='login')
def DeportesView(request):
    saludo1 = '👋 '
    saludo2 = ''
    a = azar()
    for x in a:
        saludo1 += (str(x)+', '+request.user.first_name)
        saludo2= 'Ahora sabes saludar en '+str(a[str(x)])
    data = {
        'saludo1':saludo1,
        'saludo2':saludo2,
        'm3':'active',
    }
    return render(request, 'deportes.html', data)



@login_required(login_url='login')
def CanchasView(request):
    saludo1 = '👋 '
    saludo2 = ''
    a = azar()
    c = Cancha.objects.all()
    for x in a:
        saludo1 += str(x)
        saludo2= 'Ahora sabes saludar en '+str(a[str(x)])
    data = {
        'saludo1':saludo1,
        'saludo2':saludo2,
        'm3':'active',
        'c':c,
    }
    return render(request, 'canchas.html', data)


@login_required(login_url='login')
def BloqueView(request, id):
    saludo1 = '👋 '
    saludo2 = ''
    a = azar()
    b = Horario.objects.get(id=id)
    c = Cancha.objects.get(id=b.c.id)
    for x in a:
        saludo1 += str(x)
        saludo2= 'Ahora sabes saludar en '+str(a[str(x)])
    data = {
        'saludo1':saludo1,
        'saludo2':saludo2,
        'm3':'active',
        'b':b,
        'c':c,
    }
    return render(request, 'bloque_detalle.html', data)




@login_required(login_url='login')
def CanchaView(request, id):
    saludo1 = '👋 '
    saludo2 = ''
    a = azar()
    c = Cancha.objects.get(id=id)
    import locale
    locale.setlocale(locale.LC_TIME, '')
    import datetime 
    hoy = datetime.datetime.today()
    dh = Horario.objects.filter(c=c, d=hoy)
    dh_ = dh.count()
    for x in a:
        saludo1 += str(x)
        saludo2= 'Ahora sabes saludar en '+str(a[str(x)])
    data = {
        'saludo1':saludo1,
        'saludo2':saludo2,
        'm3':'active',
        'cancha':c,
        'dh':dh,
        'dh_':dh_,
    }
    return render(request, 'cancha_detalle.html', data)



@login_required(login_url='login')
def CanchaCalendarioView(request, id):
    c = Cancha.objects.get(id=id)
    import locale
    locale.setlocale(locale.LC_TIME, '')
    import datetime 
    hoy = datetime.datetime.today()
    h1 = Horario.objects.filter(c=c, d=hoy)
    h2 = Horario.objects.filter(c=c, d=hoy+datetime.timedelta(days=1))
    h3 = Horario.objects.filter(c=c, d=hoy+datetime.timedelta(days=2))
    h4 = Horario.objects.filter(c=c, d=hoy+datetime.timedelta(days=3))
    h5 = Horario.objects.filter(c=c, d=hoy+datetime.timedelta(days=4))
    h6 = Horario.objects.filter(c=c, d=hoy+datetime.timedelta(days=5))
    h7 = Horario.objects.filter(c=c, d=hoy+datetime.timedelta(days=6))
    data = {
     
        'saludo1':'Deportes & campos deportivos'.upper(),
        'saludo2':'Experiencias, Clases, Renta de campos por horas',
        'm3':'active',
        'cancha':c,
        'h1':h1,
        'h2':h2,
        'h3':h3,
        'h4':h4,
        'h5':h5,
        'h6':h6,
        'h7':h7,
        'hoy':hoy.strftime('%A'),
        'hoy2':(hoy+datetime.timedelta(days=1)).strftime('%A'),
        'hoy3':(hoy+datetime.timedelta(days=2)).strftime("%A %d %b "),
        'hoy4':(hoy+datetime.timedelta(days=3)).strftime("%A %d %b "),
        'hoy5':(hoy+datetime.timedelta(days=4)).strftime("%A %d %b "),
        'hoy6':(hoy+datetime.timedelta(days=5)).strftime("%A %d %b "),
        'hoy7':(hoy+datetime.timedelta(days=6)).strftime("%A %d %b "),
    }
    return render(request, 'cancha_calendario.html', data)