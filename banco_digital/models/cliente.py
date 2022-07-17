from django.db import models


class Cliente(models.Model):
    PESSOA_FISICA = 'PF'
    PESSOA_JURIDICA = 'PJ'

    CLIENTE_CHOICES = [
        (PESSOA_FISICA, 'Fisica'),
        (PESSOA_JURIDICA, 'Juridica'),
    ]

    nome = models.CharField(max_length=100, null=True)
    tipo = models.CharField(
        max_length=2, choices=CLIENTE_CHOICES, default=PESSOA_FISICA)
    cpf_cnpj = models.CharField(max_length=14, null=True, unique=True)
    endereco = models.CharField(max_length=100, null=True)
    telefone = models.CharField(max_length=14, null=True)

def __str__(self) -> str:
    return self.nome