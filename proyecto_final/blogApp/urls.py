from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from blogApp.views import *
from blogApp.views import agregar_avatar
from django.conf import settings

urlpatterns = [
    # PAGINA INICIO
    path("", inicio, name="inicio"),
    path("inicio/", inicio, name="inicio"),
    
    # FORMULARIOS
    path("formulario_autor/", formulario_autor, name="formulario_autor"),
    path("formulario_articulo/", formulario_articulo, name="formulario_articulo"),
    path("formulario_seccion/", formulario_seccion, name="formulario_seccion"),
    path("buscar_seccion/", buscar_seccion, name="buscar_seccion"),
    path("resultado_busqueda_seccion/", resultado_busqueda_seccion, name="resultado_busqueda_seccion"),
    path("buscar_autor/", buscar_autor, name="buscar_autor"),
    path("resultado_busqueda_autor/", resultado_busqueda_autor, name="resultado_busqueda_autor"),
    path("buscar_articulo/", buscar_articulo, name="buscar_articulo"),
    path("resultado_busqueda_articulo/", resultado_busqueda_articulo, name="resultado_busqueda_articulo"),
    path("formulario_buscar", formulario_buscar, name="formulario_buscar"),
    
    # LOGIN / LOGOUT
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    
    # ARTICULO
    path("articulo_list", ArticuloList.as_view(), name="ArticuloList"),
    path("r'(?P<pk>\d+)^$'", ArticuloDetalle.as_view(), name="ArticuloDetalle"),
    path("editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
    path("borrar/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    
    # AUTOR
    path("autor_list", AutorList.as_view(), name="AutorList"),
    path("ver_autor/<pk>", AutorDetalle.as_view(), name="AutorDetalle"),
    path("editar_autor/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),
    path("borrar_autor/<pk>", AutorDelete.as_view(), name="AutorDelete"),
    
    # SECCION
    path("seccion_list", SeccionList.as_view(), name="SeccionList"),
    path("ver_seccion/<pk>", SeccionDetalle.as_view(), name="SeccionDetalle"),
    path("editar_seccion/<pk>", SeccionUpdateView.as_view(), name="SeccionUpdate"),
    path("borrar_seccion/<pk>", SeccionDelete.as_view(), name="SeccionDelete"),
    
    # REGISTRARSE
    path("registrarse/", register, name="Register"),
    
    # EDITAR PERFIL
    path("editar_perfil/", editar_perfil, name="EditarPerfil"),
    
    # ACERCA DE
    path("acercade/", acercade, name="AcercaDe"),
    
     # AVATAR
    path("agregar-avatar/", agregar_avatar, name="AgregarAvatar"),
]

