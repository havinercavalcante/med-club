from rest_framework.views import APIView
from usuarios.autenticacao import Autenticacao
from usuarios.serializers import UsuarioSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from usuarios.schemas.login_schemas import login_post

class Login(APIView):
    @login_post
    def post(self, request):
        nome = request.data.get('nome')
        senha = request.data.get('senha')
        
        usuario = Autenticacao.login(self, nome=nome, senha=senha)
        
        token = RefreshToken.for_user(usuario)
        
        serializer = UsuarioSerializer(usuario)
        
        return Response({
            'usuario': serializer.data,
            'refresh': str(token),
            'access': str(token.access_token)
        })
