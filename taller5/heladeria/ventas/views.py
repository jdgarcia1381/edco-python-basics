from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render

from .forms import IngredienteForm, ProductoForm, VentaForm
from .models import Ingrediente, Producto, Venta


# Create your views here.
def dashboard(request):
    productos = Producto.objects.all()
    contexto = {"productos": productos}
    return render(request, "dashboard.html", contexto)


@login_required
def custom_logout_view(request):
    logout(request)
    return redirect("ventas:login")


# INGREDIENTES
@login_required
@permission_required("ventas.view_ingrediente")
def listar_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, "ingredientes/lista.html", {"ingredientes": ingredientes})


@login_required
@permission_required("ventas.add_ingrediente")
def crear_ingrediente(request):
    if request.method == "POST":
        form = IngredienteForm(request.POST)
        if form.is_valid():
            ingrediente = form.save()
            return redirect(
                "ventas:confirmacion_ingrediente", ingrediente_id=ingrediente.id
            )
    else:
        form = IngredienteForm()

    return render(request, "ingredientes/crear.html", {"form": form})


@login_required
@permission_required("ventas.view_ingrediente")
def confirmacion_ingrediente(request, ingrediente_id):
    ingrediente = Ingrediente.objects.get(id=ingrediente_id)
    return render(
        request, "ingredientes/confirmacion.html", {"ingrediente": ingrediente}
    )


@login_required
@permission_required("ventas.view_ingrediente")
def detalle_ingrediente(request, ingrediente_id):
    ingrediente = Ingrediente.objects.get(id=ingrediente_id)
    return render(request, "ingredientes/detalle.html", {"ingrediente": ingrediente})


@login_required
@permission_required("ventas.delete_ingrediente")
def eliminar_ingrediente(request, ingrediente_id):
    ingrediente = Ingrediente.objects.get(id=ingrediente_id)
    ingrediente.delete()
    return render(
        request, "ingredientes/confirmacion_eliminar.html", {"ingrediente": ingrediente}
    )


@login_required
@permission_required("ventas.change_ingrediente")
def actualizar_ingrediente(request, ingrediente_id):
    ingrediente = Ingrediente.objects.get(id=ingrediente_id)
    if request.method == "POST":
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            ingrediente = form.save()
            return redirect(
                "ventas:confirmacion_ingrediente", ingrediente_id=ingrediente.id
            )
    else:
        form = IngredienteForm(instance=ingrediente)

    return render(request, "ingredientes/actualizar.html", {"form": form})


# PRODUCTOS
@login_required
@permission_required("ventas.view_producto")
def listar_productos(request):
    # TODO: validar el grupo para no mostrar rentabilidad
    productos = Producto.objects.all()
    return render(request, "productos/lista.html", {"productos": productos})


@login_required
@permission_required("ventas.add_producto")
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect("ventas:confirmacion_producto", producto_id=producto.id)
    else:
        form = ProductoForm()

    return render(request, "productos/crear.html", {"form": form})


@login_required
@permission_required("ventas.view_producto")
def confirmacion_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, "productos/confirmacion.html", {"producto": producto})


@login_required
@permission_required("ventas.view_producto")
def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, "productos/detalle.html", {"producto": producto})


@login_required
@permission_required("ventas.delete_producto")
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return render(
        request, "productos/confirmacion_eliminar.html", {"producto": producto}
    )


@login_required
@permission_required("ventas.change_producto")
def actualizar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect("ventas:confirmacion_producto", producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)

    return render(request, "productos/actualizar.html", {"form": form})


# VENTAS
@login_required
@permission_required("ventas.view_venta")
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "ventas/lista.html", {"ventas": ventas})


@login_required
@permission_required("ventas.add_venta")
def crear_venta(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.total = instance.cantidad * instance.producto.precio_publico
            venta = form.save()
            for ingrediente in instance.producto.ingredientes.all():
                ingrediente.inventario -= instance.cantidad
                ingrediente.save()
            return redirect("ventas:confirmacion_venta", venta_id=venta.id)
    else:
        form = VentaForm()

    return render(request, "ventas/crear.html", {"form": form})


@login_required
@permission_required("ventas.view_venta")
def confirmacion_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    return render(request, "ventas/confirmacion.html", {"venta": venta})


@login_required
@permission_required("ventas.view_venta")
def detalle_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    return render(request, "ventas/detalle.html", {"venta": venta})


@login_required
@permission_required("ventas.delete_venta")
def eliminar_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    venta.delete()
    return render(request, "ventas/confirmacion_eliminar.html", {"venta": venta})


@login_required
@permission_required("ventas.change_venta")
def actualizar_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.total = instance.cantidad * instance.producto.precio_publico
            venta = form.save()
            return redirect("ventas:confirmacion_venta", venta_id=venta.id)
    else:
        form = VentaForm(instance=venta)

    return render(request, "ventas/actualizar.html", {"form": form})
