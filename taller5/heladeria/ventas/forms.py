from django import forms

from .models import TIPOS_INGREDIENTES, TIPOS_PRODUCTOS, Ingrediente, Producto, Venta


class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = "__all__"

    def clean_sabor(self):
        tipo = self.cleaned_data["tipo"]
        sabor = self.cleaned_data["sabor"]
        if tipo != TIPOS_INGREDIENTES[0][0] and (sabor is not None):
            raise forms.ValidationError(
                "El sabor solo es permitido para el tipo de ingrediente Base"
            )
        return sabor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

    def clean_vaso(self):
        tipo = self.cleaned_data["tipo"]
        vaso = self.cleaned_data["vaso"]
        if tipo != TIPOS_PRODUCTOS[0][0] and (vaso is not None):
            raise forms.ValidationError(
                "El vaso solo es permitido para el tipo de producto Copa"
            )
        return vaso

    def clean_volumen_onzas(self):
        tipo = self.cleaned_data["tipo"]
        volumen_onzas = self.cleaned_data["volumen_onzas"]
        if tipo != TIPOS_PRODUCTOS[1][0] and (volumen_onzas is not None):
            raise forms.ValidationError(
                "El volumen (oz) solo es permitido para el tipo de producto Malteada"
            )
        return volumen_onzas


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["producto", "usuario", "cantidad"]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     cantidad = cleaned_data.get("cantidad")
    #     producto = cleaned_data.get("producto")
    #     cleaned_data["total"] = cantidad * producto.precio_publico
    #     return cleaned_data

    def clean(self):
        cleaned_data = super().clean()
        producto = self.cleaned_data.get("producto")
        cantidad = self.cleaned_data.get("cantidad")
        if not producto.tiene_inventario(cantidad):
            raise forms.ValidationError(
                "No se cuenta con inventario suficiente para registar la venta de este producto"
            )
        return cleaned_data
