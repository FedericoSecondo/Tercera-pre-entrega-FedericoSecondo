from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('libros/', libros, name="libros"),
    path('investigadores/', investigadores, name="investigadores"),
    path('prestamos/', prestamos, name="prestamos"),
    path('usuarios/', usuarios, name="usuarios"),

    path('libro_form/', libroForm, name="libro_form"),
    path('libro_form2/', libroForm2, name="libro_form2"), #VISUALIZAMOS LOS LIBROS DISPONIBLES INGRESADOS A TRAVÉS DE FORMULARIOS

    path('buscarTitulo/', buscarTitulo, name="buscarTitulo"),
    path('buscar2/', buscar2, name="buscar2"),

    path('investigadores_form/', investigadoresForm, name="investigadores_form"), #VISUALIZAMOS LOS INVESTIGADORES INGRESADOS A TRAVÉS DE FORMULARIOS
    path('usuarios_form/', usuariosForm, name="usuarios_form"), #VISUALIZAMOS LOS USUARIOS INGRESADOS A TRAVÉS DE FORMULARIOS
    path('prestamos_form/', prestamosForm, name="prestamos_form"),#VISUALIZAMOS LOS LIBROS PRESTADOS INGRESADOS A TRAVÉS DE FORMULARIOS
    
      

]
    
