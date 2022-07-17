from rest_framework import serializers
from banco_digital.models.cliente import Cliente
from banco_digital.validator.cpf_validator import valida_cpf_cnpj


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    cpf_cnpj = serializers.IntegerField
    telefone = serializers.IntegerField
    
    
    class Meta():
        model = Cliente
        fields = "__all__"
    
    def validate(self, data):
            if (data.get("tipo") == 'PJ') and len(data.get("cpf_cnpj")) != 14:
                raise serializers.ValidationError(
                    {'Tipo': 'Se tipo igual a PJ o cnpj deve ter 14 dígitos'})
            elif (data.get("tipo") == 'PF') and len(data.get("cpf_cnpj")) != 11:
                raise serializers.ValidationError(
                    'CPF deve ter 11 dígitos')
            return data
    
 
    def validate_cpf_cnpj(self, cpf_cnpj):
            if valida_cpf_cnpj(cpf_cnpj):
                raise serializers.ValidationError(
                    {'CPF': 'CPF / CNPJ deve ser numerico'})

            return cpf_cnpj

    