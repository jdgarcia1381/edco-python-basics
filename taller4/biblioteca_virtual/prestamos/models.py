from django.db import models
from libros.models import Libro
from usuarios.models import CustomUser


# Create your models here.
class Prestamo(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.usuario, self.libro, self.fecha_prestamo)
