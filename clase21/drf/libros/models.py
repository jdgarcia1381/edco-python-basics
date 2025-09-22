from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.IntegerField()
    imagen_portada = models.FileField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
