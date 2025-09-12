from django.urls import path

from .views import confirmacion_usuario, registrar_usuario

app_name = "usuarios"
urlpatterns = [
    path("registro/", registrar_usuario, name="registrar_usuario"),
    path(
        "confirmacion/<int:usuario_id>",
        confirmacion_usuario,
        name="confirmacion_usuario",
    ),  # eg. http://localhost:8000/usuarios/confirmacion/5
]
