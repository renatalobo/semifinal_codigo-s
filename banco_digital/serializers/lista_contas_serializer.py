from rest_framework import serializers
from banco_digital.models.conta import Conta


class ListaContasSerializer(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    
    class Meta:
        model = Conta
        fields = [
            'cliente',
            'conta',
            'saldo_conta',
        ]