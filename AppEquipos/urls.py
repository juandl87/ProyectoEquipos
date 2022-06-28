from django.urls import path
from AppEquipos import views

urlpatterns= [ 
    path ('',views.inicio),
    path('inicio', views.inicio),
    path ('equipo', views.equipo, name= "Equipos"),
    path ('jugadores', views.jugadores, name= "Jugadores"),
    path ('liga', views.liga, name= "Liga"), 
    path ('busquedaliga', views.busqueda_liga, name= "Busqueda Liga"),
    path ('buscar/', views.buscar),

]
