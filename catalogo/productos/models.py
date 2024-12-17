from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)  # Cantidad disponible
    estado = models.CharField(
        max_length=15, 
        choices=[('disponible', 'Disponible'), ('agotado', 'Agotado'), ('promocion', 'En promoción')],
        default='disponible'
    )  # Estado del producto
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.nombre
