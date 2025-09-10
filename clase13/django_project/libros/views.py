from django.http import HttpResponse

from .models import Libro


def index(request):
    return HttpResponse("¡Bienvenido a la Biblioteca Virtual!")


def lista_libros(request):
    libros = Libro.objects.all().order_by("name")
    return HttpResponse(libros)
