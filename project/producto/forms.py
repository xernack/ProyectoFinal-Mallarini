from django import forms

from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "categoria"]


class CategoríaForm(forms.ModelForm):
    class Meta:
        model = models.Categoría
        fields = ["nombre"]