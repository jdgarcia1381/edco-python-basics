from django import forms

from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ["usuario", "libro"]


class PrestamoUpdateForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ["usuario", "libro", "fecha_devolucion"]

        widgets = {
            "fecha_devolucion": forms.TextInput(attrs={"type": "datetime-local"}),
        }
