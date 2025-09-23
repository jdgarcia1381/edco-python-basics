from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rol = models.CharField(
        max_length=20,
        choices=[
            ("administrador", "Administrador"),
            ("bibliotecario", "Bibliotecario"),
        ],
        default="bibliotecario",
    )
    ciudad = models.CharField(max_length=100)
