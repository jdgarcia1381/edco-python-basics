from django.db import models
from django.db.models import Sum
from usuarios.models import CustomUser

TIPOS_INGREDIENTES = [
    ("Base", "Base"),
    ("Complemento", "Complemento"),
]

TIPOS_PRODUCTOS = [
    ("Copa", "Copa"),
    ("Malteada", "Malteada"),
]


# Create your models here.
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.PositiveIntegerField()
    calorias = models.PositiveIntegerField()
    inventario = models.PositiveIntegerField()
    es_vegetariano = models.BooleanField()
    es_sano = models.BooleanField()
    tipo = models.CharField(max_length=16, choices=TIPOS_INGREDIENTES)
    sabor = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return "{}".format(self.nombre)


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio_publico = models.PositiveIntegerField()
    tipo = models.CharField(max_length=8, choices=TIPOS_PRODUCTOS)
    vaso = models.CharField(max_length=200, null=True, blank=True)
    volumen_onzas = models.PositiveIntegerField(null=True, blank=True)
    ingredientes = models.ManyToManyField(Ingrediente)

    class Meta:
        pass

    def __str__(self):
        return "{}, Calorías: {}, Costo: {}, Rentabilidad: {}%".format(
            self.nombre, self.get_calorias(), self.get_costo(), self.get_rentabilidad()
        )

    def get_costo(self):
        return self.ingredientes.all().aggregate(Sum("precio")).get("precio__sum")

    def get_calorias(self):
        return self.ingredientes.all().aggregate(Sum("calorias")).get("calorias__sum")

    def get_rentabilidad(self):
        sum_precio = self.get_costo()
        return round(((self.precio_publico - sum_precio) / sum_precio) * 100, 2)

    def tiene_inventario(self, cantidad):
        for ingrediente in self.ingredientes.all():
            if ingrediente.inventario < cantidad:
                return False
        return True


class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{} - {} ({}) [{}]".format(
            self.usuario.username, self.producto.nombre, self.cantidad, self.total
        )
