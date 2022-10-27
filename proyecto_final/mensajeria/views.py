from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from django.http import HttpResponse
from mensajeria.models import Mensaje
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

def inicio_mensajeria(request):
    return render(request, "mensajeria/inicio_mensajeria.html")

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "mensajeria/mensaje_list.html"
    

@login_required
def formulario_mensaje(request):
    if request.method != "POST":
        return render(request, "mensajeria/formulario_mensaje.html")

    mensaje = Mensaje(
        destinatario=request.POST["destinatario"],
        mensaje_escrito=request.POST["mensaje_escrito"],
        fecha=request.POST["fecha"],
    )
    mensaje.save()
    return render(request, "mensajeria/inicio_mensajeria.html")
