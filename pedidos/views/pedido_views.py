from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from pedidos.models import Pedido, ItemPedido
from pedidos.serializers import PedidoSerializer, ItemPedidoSerializer
from itens.models import Item
from pedidos.schemas.schemas import list_orders_get, create_order_post, retrieve_order_get, update_order_put, delete_order_delete

class PedidoLista(APIView):
    permission_classes = [IsAuthenticated]

    @list_orders_get
    def get(self, request):
        pedidos = Pedido.objects.filter(usuario=request.user)
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    @create_order_post
    def post(self, request):
        itens_data = request.data.pop('itens', [])
        usuario = request.user
        pedido = Pedido.objects.create(usuario=usuario, total=0)

        total = 0
        for item_data in itens_data:
            item = Item.objects.get(id=item_data['item'])
            item_total = item_data['quantidade'] * item.preco
            total += item_total
            ItemPedido.objects.create(pedido=pedido, item=item, quantidade=item_data['quantidade'], preco=item.preco)
        
        pedido.total = total
        pedido.save()

        serializer = PedidoSerializer(pedido)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PedidoDetalhe(APIView):
    permission_classes = [IsAuthenticated]

    @retrieve_order_get
    def get_object(self, id):
        try:
            return Pedido.objects.get(id=id, usuario=self.request.user)
        except Pedido.DoesNotExist:
            return None

    def get(self, request, id):
        pedido = self.get_object(id)
        if pedido:
            serializer = PedidoSerializer(pedido)
            return Response(serializer.data)
        return Response({'message': 'Pedido não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @update_order_put
    def put(self, request, id):
        pedido = self.get_object(id)
        if not pedido:
            return Response({'message': 'Pedido não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @delete_order_delete
    def delete(self, request, id):
        pedido = self.get_object(id)
        if not pedido:
            return Response({'message': 'Pedido não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        pedido.delete()
        return Response({'message': 'Pedido deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
