from django.db import models

# Create your models here.

class Liga(models.Model):
    pais=models.CharField(max_length=20)
    participantes= models.IntegerField()
    fechas= models.IntegerField()

class Jugadores(models.Model):
    nombre_completo= models.CharField(max_length=45)
    nacionalidad= models.CharField(max_length=20)
    fecha_nacimiento= models.DateField()

class Equipo(models.Model):
    nombre_equipo= models.CharField(max_length=30)
    pais_origen= models.CharField(max_length=30)
    cantidad_jugadores= models.IntegerField()