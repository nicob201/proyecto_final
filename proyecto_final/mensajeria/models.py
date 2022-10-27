from secrets import choice
from django import forms
from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.forms import ChoiceField


class Mensaje(models.Model):
    class Meta:
        verbose_name_plural = "Mensajes"

    mi_lista = (("Argentina", "Argentina"), ("Brasil", "Brasil"))
    destinatario = models.CharField(max_length=100, choices=mi_lista)
    #destinatario = models.CharField(max_length=100)
    mensaje_escrito = models.CharField(max_length=100)
    fecha = models.DateField(null=True)

    def __str__(self):
        return self.destinatario


# Create your models here.
