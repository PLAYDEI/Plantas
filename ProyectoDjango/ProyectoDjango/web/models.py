from django.db import models
from django.conf import settings

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    contraseña = models.CharField(max_length=100)  # Considera usar un campo de contraseña seguro en producción
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario