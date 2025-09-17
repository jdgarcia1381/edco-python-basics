from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    rol = models.CharField(
        max_length=20,
        choices=[
            ("administrador", "Administrador"),
            ("bibliotecario", "Bibliotecario"),
        ],
        default="bibliotecario",
    )
