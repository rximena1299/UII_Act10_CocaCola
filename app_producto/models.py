from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField(blank=True, null=True)  # Puede ser nulo
    id_proveedor = models.PositiveIntegerField()

    def __str__(self):
        return f'Producto: {self.nombre_producto} ({self.categoria})'