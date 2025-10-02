from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    actualizar_ingrediente,
    actualizar_producto,
    actualizar_venta,
    confirmacion_ingrediente,
    confirmacion_producto,
    confirmacion_venta,
    crear_ingrediente,
    crear_producto,
    crear_venta,
    custom_logout_view,
    dashboard,
    detalle_ingrediente,
    detalle_producto,
    detalle_venta,
    eliminar_ingrediente,
    eliminar_producto,
    eliminar_venta,
    listar_ingredientes,
    listar_productos,
    listar_ventas,
)

app_name = "ventas"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", custom_logout_view, name="logout"),
    # INGREDIENTES
    path("ingredientes", listar_ingredientes, name="listar_ingredientes"),
    path("ingredientes/crear/", crear_ingrediente, name="crear_ingrediente"),
    path(
        "ingredientes/detalle/<int:ingrediente_id>",
        detalle_ingrediente,
        name="detalle_ingrediente",
    ),
    path(
        "ingredientes/confirmacion/<int:ingrediente_id>",
        confirmacion_ingrediente,
        name="confirmacion_ingrediente",
    ),
    path(
        "ingredientes/eliminar/<int:ingrediente_id>",
        eliminar_ingrediente,
        name="eliminar_ingrediente",
    ),
    path(
        "ingredientes/actualizar/<int:ingrediente_id>",
        actualizar_ingrediente,
        name="actualizar_ingrediente",
    ),
    # PRODUCTOS
    path("productos", listar_productos, name="listar_productos"),
    path("productos/crear/", crear_producto, name="crear_producto"),
    path(
        "productos/detalle/<int:producto_id>",
        detalle_producto,
        name="detalle_producto",
    ),
    path(
        "productos/confirmacion/<int:producto_id>",
        confirmacion_producto,
        name="confirmacion_producto",
    ),
    path(
        "productos/eliminar/<int:producto_id>",
        eliminar_producto,
        name="eliminar_producto",
    ),
    path(
        "productos/actualizar/<int:producto_id>",
        actualizar_producto,
        name="actualizar_producto",
    ),
    # VENTAS
    path("ventas", listar_ventas, name="listar_ventas"),
    path("ventas/crear/", crear_venta, name="crear_venta"),
    path(
        "ventas/detalle/<int:venta_id>",
        detalle_venta,
        name="detalle_venta",
    ),
    path(
        "ventas/confirmacion/<int:venta_id>",
        confirmacion_venta,
        name="confirmacion_venta",
    ),
    path(
        "ventas/eliminar/<int:venta_id>",
        eliminar_venta,
        name="eliminar_venta",
    ),
    path(
        "ventas/actualizar/<int:venta_id>",
        actualizar_venta,
        name="actualizar_venta",
    ),
]
