# Importar una biblioteca
#Administradora de rutas 
from django.urls import path 
#Importando vistas 

from . import views

#Declaramdo las rutas validas 
urlpatterns = [
    path("", views.index, name = "index"),
    path("author/", views.author, name = "author")
]