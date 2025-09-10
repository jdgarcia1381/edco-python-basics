from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
