from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PrestamoForm, PrestamoUpdateForm
from .models import Prestamo


# Create your views here.
def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, "prestamos/lista.html", {"prestamos": prestamos})


def registrar_prestamo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            messages.success(request, "Prestamo registrado exitosamente!")
            return redirect("prestamos:confirmacion_prestamo", prestamo_id=prestamo.id)
    else:
        form = PrestamoForm()

    return render(request, "prestamos/registrar_prestamo.html", {"form": form})


def confirmacion_prestamo(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    return render(request, "prestamos/confirmacion.html", {"prestamo": prestamo})


def detalle_prestamo(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    return render(request, "prestamos/detalle.html", {"prestamo": prestamo})


def eliminar_prestamo(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    prestamo.delete()
    return render(
        request, "prestamos/confirmacion_eliminar.html", {"prestamo": prestamo}
    )


def actualizar_prestamo(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    if request.method == "POST":
        form = PrestamoUpdateForm(request.POST, instance=prestamo)
        if form.is_valid():
            prestamo = form.save()
            messages.success(request, "Prestamo actualizado exitosamente!")
            return redirect("prestamos:confirmacion_prestamo", prestamo_id=prestamo.id)
    else:
        form = PrestamoUpdateForm(instance=prestamo)

    return render(request, "prestamos/registrar_prestamo.html", {"form": form})
