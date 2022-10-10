# Proyecto final Grupo 10 - "blogApp"

## Modelos:
### __- [ ] Autor__
### __- [ ] Articulo__
### __- [ ] Seccion__

## La aplicación cuenta con 4 paginas, __"Inicio"__, __"Autor"__, __"Sección"__ y __"Articulo"__

Las paginas de "Autor", "Sección" y "Articulo" cuentan con formularios para generar cada una de estas opciones del Blog.
    
Una vez que se completan los datos y se da clic en la opción de guardar, la aplicación almacena la información en la base de datos.


## Para realizar búsquedas en el blog:

1) __Artículos__: 
        Se debe colocar la url: http://127.0.0.1:8000/blogApp/buscar_articulo/ la cual nos lleva a un formulario donde se puede ingresar el Título de un artículo del blog para buscarlo, por ejemplo "La Escaloneta" y nos devolverá el título junto con el texto que contenga este artículo. Si se ingresa un artículo inexistente devuelve la frase "Articulo no encontrado".

2) __Autores__: 
        Se debe colocar la url: http://127.0.0.1:8000/blogApp/buscar_autor/ la cual nos lleva a un formulario donde se puede ingresar el Nombre de un autor del blog para buscarlo, por ejemplo "Lionel" y nos devolverá el nombre junto con el alias y la profesión del autor. Si se ingresa un autor inexistente devuelve la frase "Autor no encontrado".

3) __Secciones__: 
        Se debe colocar la url: http://127.0.0.1:8000/blogApp/buscar_seccion/ la cual nos lleva a un formulario donde se puede ingresar el Nombre de una sección del blog para buscarla, por ejemplo "Deportes" y nos devolverá el nombre. Si se ingresa una sección inexistente devuelve la frase "Seccion no encontrada".

## El formato de las distintas páginas se heredan de __padre.html__, el cual fija la navbar y el footer.

## INTEGRANTES DEL GRUPO:
### - Benini Nicolás
### - Boscasso Nicolás