from rest_framework import generics
from banco_digital.models.conta import Conta
from banco_digital.serializers.lista_contas_serializer import ListaContasSerializer


class ListaContasViewset(generics.ListAPIView):
    """Listando as contas"""

    def get_queryset(self):
        queryset = Conta.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaContasSerializer