from django.contrib import admin
from django.urls import path, include

from blogApp.views import (
    inicio,
    formulario_autor,
    formulario_articulo,
    formulario_seccion,
    busqueda_autor,
)

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("formulario_autor/", formulario_autor, name="formulario_autor"),
    path("formulario_articulo/", formulario_articulo, name="formulario_articulo"),
    path("formulario_seccion/", formulario_seccion, name="formulario_seccion"),
    path("busqueda_autor/", busqueda_autor, name="busqueda_autor"),
]
