# pedidos/urls.py
from django.urls import path
from pedidos.views.pedido_views import PedidoLista, PedidoDetalhe

urlpatterns = [
    path('pedidos', PedidoLista.as_view(), name='pedido-lista'),
    path('pedidos/<int:id>', PedidoDetalhe.as_view(), name='pedido-detalhe'),
]
