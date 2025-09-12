from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Libro


def index(request):
    mensaje = "Bienvenido a nuestra biblioteca virtual"
    return HttpResponse(f"<h1>{mensaje}</h1><p>Tu portal de conocimiento</p>")


def lista_libros(request):
    # libros = Libro.objects.all().order_by("titulo")
    # return HttpResponse(libros)

    libros = Libro.objects.all()
    html = "<ul>"
    for libro in libros:
        html += f"<li>{libro.titulo}</li>"
    html += "</ul>"
    return HttpResponse(html)


def libros_disponibles(request):
    libros = Libro.objects.filter(disponible=True)
    contexto = {"libros": libros}
    return render(request, "libros.html", contexto)


class LibrosDisponiblesView(ListView):
    model = Libro
    template_name = "libros.html"
    queryset = Libro.objects.filter(disponible=True)
