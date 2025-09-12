from django.urls import path

from .views import (
    confirmacion_libro,
    detalle_libro,
    eliminar_libro,
    listar_libros,
    registrar_libro,
)

app_name = "libros"
urlpatterns = [
    path("", listar_libros, name="listar_libros"),
    path("registro/", registrar_libro, name="registrar_libro"),
    path(
        "detalle/<int:libro_id>",
        detalle_libro,
        name="detalle_libro",
    ),
    path(
        "confirmacion/<int:libro_id>",
        confirmacion_libro,
        name="confirmacion_libro",
    ),  # eg. http://localhost:8000/libros/confirmacion/5
    path(
        "eliminar/<int:libro_id>",
        eliminar_libro,
        name="eliminar_libro",
    ),
]
