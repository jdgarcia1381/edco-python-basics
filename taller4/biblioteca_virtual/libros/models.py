from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    anio_publicacion = models.SmallIntegerField()

    def __str__(self):
        return "{} - {} ({})".format(self.titulo, self.autor, self.anio_publicacion)
