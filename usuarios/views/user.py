from rest_framework.views import APIView
from usuarios.serializers import UsuarioSerializer
from usuarios.models import Usuario
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from usuarios.schemas.user_schemas import retrieve_user_schema, update_user_schema, delete_user_schema

class User(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(**retrieve_user_schema)
    def get(self, request) -> None:
        usuario = Usuario.objects.filter(id=request.user.id).first()
        serializer = UsuarioSerializer(usuario)
        return Response({'usuario': serializer.data})

    @swagger_auto_schema(**update_user_schema)
    def put(self, request, id):
        usuario = Usuario.objects.filter(id=id).first()
        if usuario:
            serializer = UsuarioSerializer(usuario, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Usuário atualizado com sucesso'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(**delete_user_schema)
    def delete(self, request, id):
        usuario = Usuario.objects.filter(id=id).first()
        if usuario:
            usuario.delete()
            return Response({'message': 'Usuário deletado com sucesso'})
        return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
