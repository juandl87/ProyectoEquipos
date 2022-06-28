from urllib import response 
from django.http import HttpResponse    
from django.shortcuts import render

from AppEquipos.forms import Formulario_equipo, Formulario_liga, Formulario_jugadores
from AppEquipos.models import Equipo, Liga, Jugadores


# Create your views here.
def inicio (request):
    return render(request, "AppEquipos/inicio.html")

def equipo (request):
    return render(request,"AppEquipos/equipo.html")

def jugadores (request):
    return render(request, "AppEquipos/jugadores.html")

def liga (request):
    return render(request, "AppEquipos/liga.html")

def liga(request):

    if request.method == 'POST':
        formulario_liga= Formulario_liga(request.POST)
        print(formulario_liga)

        if formulario_liga.is_valid:
            info_liga= formulario_liga.cleaned_data

            ligadat= Liga (pais= info_liga['pais'], participantes= info_liga['participantes'], fechas= info_liga['fechas'])
            ligadat.save()

            return render (request, "AppEquipos/inicio.html")
    else:
        formulario_liga=Formulario_liga()
    return render(request, "AppEquipos/liga.html", {"formulario_liga":formulario_liga})

def equipo(request):

    if request.method == 'POST':
        formulario_equipo= Formulario_equipo(request.POST)
        print(formulario_equipo)

        if formulario_equipo.is_valid:
            info_equipo= formulario_equipo.cleaned_data

            equipodat= Equipo (nombre_equipo= info_equipo['nombre_equipo'], pais_origen= info_equipo['nombre_equipo'], cantidad_jugadores= info_equipo['cantidad_jugadores'])
            equipodat.save()

            return render (request, "AppEquipos/inicio.html")
    else:
        formulario_equipo=Formulario_equipo()
    return render(request, "AppEquipos/equipo.html", {"formulario_equipo":formulario_equipo})    

def jugadores(request):

    if request.method == 'POST':
        formulario_jugadores= Formulario_jugadores(request.POST)
        print(formulario_jugadores)

        if formulario_jugadores.is_valid:
            info_jugadores= formulario_jugadores.cleaned_data

            jugadoresdat= Jugadores (nombre_completo= info_jugadores['nombre_completo'], nacionalidad= info_jugadores['nacionalidad'], fecha_nacimiento= info_jugadores['fecha_nacimiento'])
            jugadoresdat.save()

            return render (request, "AppEquipos/inicio.html")
    else:
        formulario_jugadores=Formulario_jugadores()
    return render(request, "AppEquipos/jugadores.html", {"formulario_jugadores":formulario_jugadores})

def busqueda_liga(request):
    return render(request, "busqueda_liga.html")

def buscar (request):

    if request.GET["pais"]:
        pais= request.GET['pais']
        ligas= Liga.objects.filter(pais__icontains=pais)

        return render (request, "AppEquipos/resultadobusqueda.html", {"ligas":ligas, "pais":pais})
    
    else:
        respuesta="no enviaste datos"
    
    return HttpResponse(respuesta)
    
   


        








            