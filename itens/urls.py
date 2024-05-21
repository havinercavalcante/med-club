from django.urls import path
from itens.views.item_views import ItemLista, ItemDetalhe

urlpatterns = [
    path('itens', ItemLista.as_view(), name='item-list'),
    path('itens/<int:id>', ItemDetalhe.as_view(), name='item-detail'),
]
