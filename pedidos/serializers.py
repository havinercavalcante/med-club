# pedidos/serializers.py
from rest_framework import serializers
from .models import Pedido, ItemPedido
from itens.models import Item

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = ('item', 'quantidade', 'preco')

class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ('id', 'usuario', 'data_criacao', 'total', 'itens')
        read_only_fields = ('total', 'usuario', 'data_criacao')
