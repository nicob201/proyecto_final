from django.contrib import admin
from django.urls import path, include

from blogApp.views import (
    inicio,
    formulario_autor,
    formulario_articulo,
    formulario_seccion,
    buscar_seccion,
    resultado_busqueda_seccion,
    buscar_autor,
    resultado_busqueda_autor,
    buscar_articulo,
    resultado_busqueda_articulo,
    MyLogin,
    MyLogout,
    ArticuloList,
    ArticuloDetalle,
    ArticuloCreacion,
    ArticuloUpdateView,
    ArticuloDelete,
    formulario_buscar,
)

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("formulario_autor/", formulario_autor, name="formulario_autor"),
    path("formulario_articulo/", formulario_articulo, name="formulario_articulo"),
    path("formulario_seccion/", formulario_seccion, name="formulario_seccion"),
    path("buscar_seccion/", buscar_seccion, name="buscar_seccion"),
    path(
        "resultado_busqueda_seccion/",
        resultado_busqueda_seccion,
        name="resultado_busqueda_seccion",
    ),
    path("buscar_autor/", buscar_autor, name="buscar_autor"),
    path(
        "resultado_busqueda_autor/",
        resultado_busqueda_autor,
        name="resultado_busqueda_autor",
    ),
    path("buscar_articulo/", buscar_articulo, name="buscar_articulo"),
    path(
        "resultado_busqueda_articulo/",
        resultado_busqueda_articulo,
        name="resultado_busqueda_articulo",
    ),
    
    
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    
    
    path("articulo_list", ArticuloList.as_view(), name="ArticuloList"),
    path("r'(?P<pk>\d+)^$'", ArticuloDetalle.as_view(), name="ArticuloDetalle"),
    path("articulo_creacion", ArticuloCreacion.as_view(), name="ArticuloCreacion"),
    path("editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
    path("borrar/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    path("formulario_buscar", formulario_buscar, name="formulario_buscar"),
]
