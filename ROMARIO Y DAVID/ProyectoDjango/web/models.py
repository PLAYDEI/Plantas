from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario