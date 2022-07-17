from rest_framework import viewsets, filters
from banco_digital.models.conta import Conta
from banco_digital.serializers.conta_serializer import ContaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    queryset = Conta.objects.all()

    filter_backends = [
            DjangoFilterBackend,
            filters.OrderingFilter,
            filters.SearchFilter
        ]
    search_fields = ['conta', 'cliente']
    ordering_fields = ['conta']


