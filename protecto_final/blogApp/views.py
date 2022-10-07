from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Autor, Articulo, Seccion


def inicio(request):
    return render(request, "blogApp/inicio.html")


def formulario_autor(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_autor.html")

    nombre = Autor(nombre=request.POST["nombre"], alias=request.POST["alias"], profesion=request.POST["profesion"])
    nombre.save()
    return render(request, "blogApp/inicio.html")

    
def formulario_articulo(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_articulo.html")

    articulo = Articulo(texto=request.POST["texto"], titulo=request.POST["titulo"], fecha=request.POST["fecha"])
    articulo.save()
    return render(request, "blogApp/inicio.html")


def formulario_seccion(request):
    if request.method != "POST":
        return render(request, "blogApp/formulario_seccion.html")

    seccion = Seccion(nombre=request.POST["nombre"])
    seccion.save()
    return render(request, "blogApp/inicio.html")


def busqueda_autor(request):

    if not request.GET["nombre"]:
         return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        autores = Autor.objects.filter(nombre=nombre_a_buscar)


        contexto = {
            "nombre": nombre_a_buscar,
            "autores_encontrados": autores
        }
        
        return render(request, "blogApp/resultado_busqueda.html", contexto)