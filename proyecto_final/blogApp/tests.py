from django.test import TestCase
from datetime import datetime
from django.test import TestCase
from blogApp.models import *


class ViewTestCase(TestCase):

    def test_crear_articulo(self):
        Articulo.objects.create(titulo="test 1234", texto="abcd-9091", fecha='2022/11/19')
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].titulo == "test 1234"
        
    print('*' * 90)


    def test_crear_articulo_sin_duracion(self):
        Articulo.objects.create(titulo="test 1234", texto="9091", fecha='2022/11/19')
        todos_los_articulos = Articulo.objects.all()
        assert todos_los_articulos[0].duracion is None
        
    print('.' * 90)


    """ def test_crear_4_articulos(self):
        Articulo.objects.create(titulo="test 1", texto="abcd-1", fecha="1/04/2022")
        Articulo.objects.create(titulo="test 2", texto="abcd-2", fecha="2/04/2022")
        Articulo.objects.create(titulo="test 3", texto="abcd-3", fecha="3/04/2022")
        Articulo.objects.create(titulo="test 4", texto="abcd-4", fecha="4/04/2022")
        Articulo.objects.create(titulo="test 5", texto="abcd-5", fecha="5/04/2022")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 5
        
        
    print('#' * 90) """