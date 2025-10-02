from django.contrib import admin

from .models import Ingrediente, Producto, Venta

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(Producto)
admin.site.register(Venta)
