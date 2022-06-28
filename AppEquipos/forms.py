from django import forms

class Formulario_liga (forms.Form):
    pais=forms.CharField(max_length=20)
    participantes= forms.IntegerField()
    fechas= forms.IntegerField()

class Formulario_jugadores (forms.Form):
    nombre_completo= forms.CharField(max_length=45)
    nacionalidad= forms.CharField(max_length=20)
    fecha_nacimiento= forms.DateField()

class Formulario_equipo (forms.Form):
    nombre_equipo= forms.CharField(max_length=30)
    pais_origen= forms.CharField(max_length=30)
    cantidad_jugadores= forms.IntegerField()