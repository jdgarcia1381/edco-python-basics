from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    rol = models.CharField(
        max_length=16,
        choices=[
            ("Administrador", "Administrador"),
            ("Empleado", "Empleado"),
            ("Cliente", "Cliente"),
        ],
        default="Cliente",
    )
