from django.contrib import admin

from .models import Libro

# Register your models here.
# admin.register(Libro) # Incorrecto
admin.site.register(Libro)  # Correcto
