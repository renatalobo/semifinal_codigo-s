from warnings import filters
from rest_framework import viewsets, filters
from banco_digital.models.cliente import Cliente
from banco_digital.serializers.cliente_serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend 


class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

    filter_backends = [
            DjangoFilterBackend,
            filters.OrderingFilter,
            filters.SearchFilter
        ]
    search_fields = ['nome', 'endereco']
    ordering_fields = ['nome']
    