from django.test import TestCase
from datetime import *
from blogApp.models import *


class ViewTestCase(TestCase):
    
    # TEST N°1
    def test_crear_seccion(self):
        Seccion.objects.create(nombre="Prueba123")
        todas_las_secciones = Seccion.objects.all()
        assert len(todas_las_secciones) == 1
        assert todas_las_secciones[0].nombre == "Prueba123"


    # TEST N°2
    def test_crear_articulo(self):
        Articulo.objects.create(titulo="test1234", texto="abcd-9091", fecha=None)
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].titulo == "test1234"
    
    
    # TEST N°3
    def test_crear_seccion_sin_nombre(self):
        Seccion.objects.create(nombre="")
        todas_las_secciones = Seccion.objects.all()
        assert todas_las_secciones[0].nombre == ""
    
    
    # TEST N°4
    def test_crear_articulo_sin_fecha(self):
        Articulo.objects.create(titulo="test 1234", texto="9091")
        todos_los_articulos = Articulo.objects.all()
        assert todos_los_articulos[0].fecha is None


    # TEST N°5
    def test_crear_3_secciones(self):
        Seccion.objects.create(nombre="Prueba1")
        Seccion.objects.create(nombre="Prueba2")
        Seccion.objects.create(nombre="Prueba3")
        todas_las_secciones = Seccion.objects.all()
        assert len(todas_las_secciones) == 3
    
    
    # TEST N°6
    def test_crear_4_articulos(self):
        Articulo.objects.create(titulo="test 1", texto="abcd-1")
        Articulo.objects.create(titulo="test 2", texto="abcd-2")
        Articulo.objects.create(titulo="test 3", texto="abcd-3")
        Articulo.objects.create(titulo="test 4", texto="abcd-4")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 4