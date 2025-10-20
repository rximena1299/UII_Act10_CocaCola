from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre_producto',
            'categoria',
            'precio_unitario',
            'stock_actual',
            'fecha_vencimiento',
            'id_proveedor'
        ]
        labels = {
            'nombre_producto': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio_unitario': 'Precio Unitario',
            'stock_actual': 'Stock Actual',
            'fecha_vencimiento': 'Fecha de Vencimiento',
        '   id_proveedor': 'ID del Proveedor'
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}), # Permite decimales
            'stock_actual': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}), # Stock no puede ser negativo
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # Input de fecha HTML5
            'id_proveedor': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}), # ID de proveedor positivo
        }