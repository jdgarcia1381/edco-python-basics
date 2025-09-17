from django.contrib import admin

from .models import Libro


# Register your models here.
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "anio_publicacion")
    search_fields = ("titulo", "autor")
    list_filter = ("anio_publicacion",)
    ordering = ["anio_publicacion", "titulo"]


admin.site.register(Libro, LibroAdmin)
