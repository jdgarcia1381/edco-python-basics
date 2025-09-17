from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "documento",
            "telefono",
            "rol",
            "password1",
            "password2",
        )


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "documento",
            "telefono",
            "rol",
            "first_name",
            "last_name",
        )
