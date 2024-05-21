from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from itens.models import Item
from itens.serializers import ItemSerializer
from itens.schemas.schemas import list_items_get, create_item_post, retrieve_item_get, update_item_put, delete_item_delete

class ItemLista(APIView):
    permission_classes = [IsAuthenticated]

    @list_items_get
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @create_item_post
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetalhe(APIView):
    permission_classes = [IsAuthenticated]

    @retrieve_item_get
    def get_object(self, id):
        try:
            return Item.objects.get(id=id)
        except Item.DoesNotExist:
            return None

    def get(self, request, id):
        item = self.get_object(id)
        if item:
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @update_item_put
    def put(self, request, id):
        item = self.get_object(id)
        if item:
            serializer = ItemSerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Item atualizado com sucesso',
                    'item': serializer.data
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Item não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @delete_item_delete
    def delete(self, request, id):
        item = self.get_object(id)
        if item:
            item.delete()
            return Response({'message': 'Item deletado com sucesso'}, status=status.HTTP_200_OK)
        return Response({'message': 'Item não encontrado'}, status=status.HTTP_404_NOT_FOUND)
