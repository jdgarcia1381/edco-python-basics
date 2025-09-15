from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import LibroForm
from .models import Libro


# Create your views here.
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/lista.html", {"libros": libros})


def registrar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            messages.success(request, "Libro registrado exitosamente!")
            return redirect("libros:confirmacion_libro", libro_id=libro.id)
    else:
        form = LibroForm()

    return render(request, "libros/registrar_libro.html", {"form": form})


def confirmacion_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    return render(request, "libros/confirmacion.html", {"libro": libro})


def detalle_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    return render(request, "libros/detalle.html", {"libro": libro})


def eliminar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    libro.delete()
    return render(request, "libros/confirmacion_eliminar.html", {"libro": libro})


def actualizar_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            messages.success(request, "Libro actualizado exitosamente!")
            return redirect("libros:confirmacion_libro", libro_id=libro.id)
    else:
        form = LibroForm(instance=libro)

    return render(request, "libros/actualizar_libro.html", {"form": form})
