# forms.py
from django import forms

from .models import Usuario


# Formulario Genérico
class RegistroUsuarioBaseForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ingresa tu nombre"}
        ),
    )
    correo = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    edad = forms.IntegerField(min_value=18, max_value=120)


# Formulario basado en Modelo
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "correo", "edad"]
        widgets = {"nombre": forms.TextInput(attrs={"class": "form-control"})}

    def clean_correo(self):
        correo = self.cleaned_data["correo"]
        if Usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return correo

    def clean_edad(self):
        edad = self.cleaned_data["edad"]
        if edad < 18:
            raise forms.ValidationError("Debes ser mayor de edad para registrarte.")
        return edad


class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "correo", "edad"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tu nombre completo"}
            ),
            "correo": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "tu@email.com"}
            ),
            "edad": forms.NumberInput(
                attrs={"class": "form-control", "min": "18", "max": "120"}
            ),
        }
