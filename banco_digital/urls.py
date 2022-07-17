from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from banco_digital.views.cliente_views import ClienteViewSet
from banco_digital.views.conta_views import ContaViewSet
from banco_digital.views.lista_contas_viewset import ListaContasViewset
from banco_digital.views.transacao_views import TransacaoViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'contas', ContaViewSet)
router.register(r'transacoes', TransacaoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('clientes/<int:pk>/contas/', ListaContasViewset.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
