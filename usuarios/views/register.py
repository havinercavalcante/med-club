from rest_framework.views import APIView
from usuarios.views.autenticacao import Autenticacao
from usuarios.serializers import UsuarioSerializer
from rest_framework.response import Response
from usuarios.schemas.register_schemas import register_post

class Register(APIView):
    @register_post
    def post(self, request):
        nome = request.data.get('nome')
        email = request.data.get('email')
        senha = request.data.get('senha')
        
        usuario = Autenticacao.register(self, nome=nome, email=email, senha=senha)
        
        serializer = UsuarioSerializer(usuario)
        
        return Response({'usuario': serializer.data})
