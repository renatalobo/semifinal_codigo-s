from contextlib import nullcontext
from rest_framework import serializers
from banco_digital.models.conta import Conta
from banco_digital.models.transacao import Transacao


class TransacaoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta():
        model = Transacao
        fields = '__all__'

      
    def validate(self, data):
            if (data.get("conta_origem")) == (data.get("conta_destino")):
                raise serializers.ValidationError(
                    {'Conta destino deve ser diferente da conta origem'})

            return data


    def create(self, validated_data):
        conta_origem = Conta.objects.get(conta__exact=validated_data['conta_origem'])
        conta_destino = Conta.objects.get(conta__exact=validated_data['conta_destino'])

        conta_origem.saldo_conta -= validated_data['valor']
        
        if conta_origem.saldo_conta <= 0:
            raise serializers.ValidationError({'Saldo insuficiente!'})

        conta_destino.saldo_conta += validated_data['valor']
        conta_origem.save()
        conta_destino.save()

        return super().create(validated_data)


    def validate_conta(self, validated_data):
        conta_origem = Conta.objects.get(conta__exact=validated_data['conta_origem'])
        conta_destino = Conta.objects.get(conta__exact=validated_data['conta_destino'])
             
        if conta_origem.conta == "":
            raise serializers.ValidationError({'Conta de origem não existe'})
        elif conta_destino.conta == "":
            raise serializers.ValidationError({'Conta destino não existe'})
   