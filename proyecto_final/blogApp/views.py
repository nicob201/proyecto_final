from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Autor, Articulo, Seccion
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from blogApp.forms import *
from blogApp.models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)



# PAGINA DE INICIO DEL BLOG
@login_required
def inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        contexto = {"avatar": avatar.imagen.url}
    else:
        contexto = {}

    return render(request, "blogApp/inicio.html", contexto)


##########################################################
# FORMULARIOS DE INGRESO DE DATOS
##########################################################

# CREACION DE UN NUEVO AUTOR
@login_required
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
@login_required
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
@login_required
def formulario_seccion(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_seccion.html")

    seccion = Seccion(nombre=request.POST["nombre"])
    seccion.save()
    return render(request, "blogApp/inicio.html")


# FORMULARIOS DE BUSQUEDA

##########################################################
# BUSQUEDA EN SECCIONES
##########################################################
@login_required
def buscar_seccion(request):
    return render(request, "blogApp/buscar_seccion.html")


@login_required
def resultado_busqueda_seccion(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        nombre_encontrado = Seccion.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "seccion_encontrada": nombre_encontrado}

        return render(request, "blogApp/resultado_busqueda_seccion.html", contexto)


##########################################################
# BUSQUEDA EN AUTORES
##########################################################
@login_required
def buscar_autor(request):
    return render(request, "blogApp/buscar_autor.html")


@login_required
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


##########################################################
# BUSQUEDA EN ARTICULOS
##########################################################
@login_required
def buscar_articulo(request):
    return render(request, "blogApp/buscar_articulo.html")


@login_required
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


class MyLogout(LoginRequiredMixin, LogoutView):
    template_name = "blogApp/logout.html"


##########################################################
# BUSQUEDA GENERAL
##########################################################
@login_required
def formulario_buscar(request):
    return render(request, "blogApp/buscar_general.html")


##########################################################
# ARTICULOS - EDITAR - BORAR - ACTUALIZAR
##########################################################
class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = "blogApp/articulo_list.html"


class ArticuloDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = "blogApp/articulo_detalle.html"


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = "/blogApp/articulo_list"
    fields = ["titulo", "texto"]


class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = "/blogApp/articulo_list"


##########################################################
# AUTOR - EDITAR - BORAR - ACTUALIZAR
##########################################################
class AutorList(LoginRequiredMixin, ListView):
    model = Autor
    template_name = "blogApp/autor_list.html"


class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = "blogApp/autor_detalle.html"


class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/blogApp/autor_list"
    fields = ["nombre", "alias", "profesion"]


class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/blogApp/autor_list"
    

##########################################################
# SECCION - EDITAR - BORAR - ACTUALIZAR
##########################################################
class SeccionList(LoginRequiredMixin, ListView):
    model = Seccion
    template_name = "blogApp/seccion_list.html"


class SeccionDetalle(LoginRequiredMixin, DetailView):
    model = Seccion
    template_name = "blogApp/seccion_detalle.html"


class SeccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Seccion
    success_url = "/blogApp/seccion_list"
    fields = ["nombre"]


class SeccionDelete(LoginRequiredMixin, DeleteView):
    model = Seccion
    success_url = "/blogApp/seccion_list"


##########################################################
# REGISTRARSE
##########################################################
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return render(
                request,
                "blogApp/inicio.html",
            )

    else:
        form = SignUpForm()

    return render(request, "blogApp/registro.html", {"form": form})


##########################################################
# EDITAR PERFIL
##########################################################
@login_required
def editar_perfil(request):
    user = request.user
    
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blogApp/inicio.html")

    contexto = {
        "user": user,
        "form": form
    }
    return render(request, "blogApp/editarPerfil.html", contexto)


##########################################################
# AVATAR
##########################################################
@login_required
def agregar_avatar(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blogApp/inicio.html")

    contexto = {
                "form": form,
                "avatar": avatar.imagen.url
                }
    return render(request, "blogApp/avatar_form.html", contexto)


##########################################################
# ACERCA DE
##########################################################
@login_required
def acercade(request):
    return render(request, "blogApp/acercade.html")