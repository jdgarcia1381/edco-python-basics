from django.contrib import admin

from .models import Prestamo


# Register your models here.
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("libro", "usuario", "fecha_prestamo", "fecha_devolucion")
    list_filter = ("fecha_prestamo",)
    search_fields = ("libro__titulo", "usuario__username")


admin.site.register(Prestamo, PrestamoAdmin)
