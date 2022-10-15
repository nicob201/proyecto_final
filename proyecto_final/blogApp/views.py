from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Autor, Articulo, Seccion
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# PAGINA DE INICIO DEL BLOG
def inicio(request):
    return render(request, "blogApp/inicio.html")

##########################################################
# FORMULARIOS DE INGRESO DE DATOS
##########################################################

# CREACION DE UN NUEVO AUTOR
def formulario_autor(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_autor.html")

    nombre = Autor(
        nombre=request.POST["nombre"],
        alias=request.POST["alias"],
        profesion=request.POST["profesion"],
    )
    nombre.save()
    return render(request, "blogApp/inicio.html")


# CREACION DE UN NUEVO ARTICULO
def formulario_articulo(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_articulo.html")

    articulo = Articulo(
        texto=request.POST["texto"],
        titulo=request.POST["titulo"],
        fecha=request.POST["fecha"],
    )
    articulo.save()
    return render(request, "blogApp/inicio.html")


# CREACION DE UNA NUEVA SECCION
def formulario_seccion(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_seccion.html")

    seccion = Seccion(nombre=request.POST["nombre"])
    seccion.save()
    return render(request, "blogApp/inicio.html")



##########################################################
# FORMULARIOS DE BUSQUEDA
##########################################################

# BUSQUEDA EN SECCIONES
def buscar_seccion(request):
    return render(request, "blogApp/buscar_seccion.html")


def resultado_busqueda_seccion(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        nombre_encontrado = Seccion.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "seccion_encontrada": nombre_encontrado}

        return render(request, "blogApp/resultado_busqueda_seccion.html", contexto)


# BUSQUEDA EN AUTORES
def buscar_autor(request):
    return render(request, "blogApp/buscar_autor.html")


def resultado_busqueda_autor(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        autor_a_buscar = request.GET["nombre"]
        nombre_autor_encontrado = Autor.objects.filter(nombre=autor_a_buscar)

        contexto = {
            "nombre": autor_a_buscar,
            "autor_encontrado": nombre_autor_encontrado,
        }

        return render(request, "blogApp/resultado_busqueda_autor.html", contexto)


# BUSQUEDA EN ARTICULOS
def buscar_articulo(request):
    return render(request, "blogApp/buscar_articulo.html")


def resultado_busqueda_articulo(request):

    if not request.GET["titulo"]:
        return HttpResponse("No enviaste datos")
    else:
        articulo_a_buscar = request.GET["titulo"]
        info_articulo_encontrado = Articulo.objects.filter(titulo=articulo_a_buscar)

        contexto = {
            "titulo": articulo_a_buscar,
            "articulo_encontrado": info_articulo_encontrado,
        }

        return render(request, "blogApp/resultado_busqueda_articulo.html", contexto)

##########################################################
# LOGIN Y LOGOUT
##########################################################
class MyLogin(LoginView):
    template_name = "blogApp/login.html"


class MyLogout(LogoutView, LoginRequiredMixin):
    template_name = "blogApp/logout.html"
    


##########################################################
# EDITAR - BORAR - ACTUALIZAR
##########################################################
class ArticuloList(ListView, LoginRequiredMixin):
    model = Articulo
    template_name = "blogApp/articulo_list.html"


class ArticuloDetalle(DetailView, LoginRequiredMixin):
    model = Articulo
    template_name = "blogApp/articulo_detalle.html"


class ArticuloCreacion(CreateView, LoginRequiredMixin):
    model = Articulo
    fields = ["titulo", "texto", "fecha"]
    success_url = "/blogApp/Articulo/list"


class ArticuloUpdateView(UpdateView, LoginRequiredMixin):
    model = Articulo
    success_url = "/blogApp/articulo_list"
    fields = ["titulo", "texto"]


class ArticuloDelete(DeleteView, LoginRequiredMixin):

    model = Articulo
    success_url = "/blogApp/articulo_list"
    
    
    
    
def formulario_buscar(request):
    return render(request, "blogApp/buscar_general.html")