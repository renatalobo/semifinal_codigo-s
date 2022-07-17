import datetime
from django.db import models
from banco_digital.models.conta import Conta


class Transacao(models.Model):
    conta_origem = models.CharField(max_length=20, null=False)
    conta_destino = models.CharField(max_length=20, null=False)
    data_transacao = models.DateField(default=datetime.date.today, null=False)
    valor = models.FloatField(null=False)
    
    class Meta():
        verbose_name_plural = "Transações"
