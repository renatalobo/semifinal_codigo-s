import datetime
from django.db import models
from banco_digital.models.cliente import Cliente


class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    conta = models.CharField(max_length=20, null=True, unique=True)
    deposito_inicial = models.FloatField(null=True, default=0)
    data_abertura = models.DateField(default=datetime.date.today, null=False)
    saldo_conta = models.FloatField(default=0)
    