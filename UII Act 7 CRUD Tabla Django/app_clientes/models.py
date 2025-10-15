from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    sandwich_favorito = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Cliente: {self.nombre} - {self.telefono}'