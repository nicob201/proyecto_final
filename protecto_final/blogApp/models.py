from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=40)
    alias = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre, self.apellido


class Articulo(models.Model):
    class Meta:
        verbose_name_plural = "Articulos"

    titulo = models.CharField(max_length=40)
    texto = models.CharField(max_length=1000)
    fecha = models.DateField(null=True)


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=40)
