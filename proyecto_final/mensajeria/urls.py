from django.contrib import admin
from django.urls import path, include

from mensajeria.views import *
from blogApp.views import MyLogin, MyLogout

urlpatterns = [
    path("inicio_mensajeria/", inicio_mensajeria, name="inicio_mensajeria"),
    path("mensaje_list", MensajeList.as_view(), name="MensajeList"),
    path("formulario_mensaje/", formulario_mensaje, name="formulario_mensaje"),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
]