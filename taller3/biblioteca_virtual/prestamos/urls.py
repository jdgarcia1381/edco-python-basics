from django.urls import path

from .views import (
    actualizar_prestamo,
    confirmacion_prestamo,
    detalle_prestamo,
    eliminar_prestamo,
    listar_prestamos,
    registrar_prestamo,
)

app_name = "prestamos"
urlpatterns = [
    path("", listar_prestamos, name="listar_prestamos"),
    path("registro/", registrar_prestamo, name="registrar_prestamo"),
    path(
        "detalle/<int:prestamo_id>",
        detalle_prestamo,
        name="detalle_prestamo",
    ),
    path(
        "confirmacion/<int:prestamo_id>",
        confirmacion_prestamo,
        name="confirmacion_prestamo",
    ),  # eg. http://localhost:8000/prestamos/confirmacion/5
    path(
        "eliminar/<int:prestamo_id>",
        eliminar_prestamo,
        name="eliminar_prestamo",
    ),
    path(
        "actualizar/<int:prestamo_id>", actualizar_prestamo, name="actualizar_prestamo"
    ),
]
