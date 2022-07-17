from rest_framework import serializers
from banco_digital.models.conta import Conta


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
            
            validated_data['saldo_conta'] = validated_data['deposito_inicial']
            return super().create(validated_data)

    class Meta():
        model = Conta
        fields = [
            'cliente',
            'conta',
            'deposito_inicial',
            'data_abertura',
            'saldo_conta'   
        ]

        read_only_fields = ['saldo_conta']



        