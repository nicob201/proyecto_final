from django.contrib import admin
from django.urls import path, include
from mensajeria.views import *
from blogApp.views import *

urlpatterns = [
    path("inicio_mensajeria/", inicio_mensajeria, name="inicio_mensajeria"),
    path("mensaje_list", MensajeList.as_view(), name="MensajeList"),
    path("formulario_mensaje/", formulario_mensaje, name="formulario_mensaje"),
]
