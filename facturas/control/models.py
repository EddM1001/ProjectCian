from django.db import models
from django.conf import settings
from django.utils import timezone

# Aqui creamos los modelos cliente y fatura 
# con sus respectivos campos
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tarifa = models.IntegerField()
    watts = models.IntegerField()