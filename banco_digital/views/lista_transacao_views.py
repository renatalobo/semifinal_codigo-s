from rest_framework import generics
from banco_digital.models.transacao import Transacao
from banco_digital.serializers.lista_contas_serializer import ListaContasSerializer

class ListaTransacaoViewSet(generics.ListAPIView):
    """Listando as contas"""

    def get_queryset(self):
        queryset = Transacao.objects.filter(conta_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaContasSerializer