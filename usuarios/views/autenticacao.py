from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password
from usuarios.models import Usuario

class Autenticacao:
    def login(self, nome=None, senha=None) -> Usuario:
        erro_validacao = AuthenticationFailed('Email e/ou senha incorreto(s)')

        usuario = Usuario.objects.filter(nome=nome).first()
        
        if not usuario or not check_password(senha, usuario.password):
            raise erro_validacao
        
        if not check_password(senha, usuario.password):
            raise erro_validacao

        return usuario
    

    def register(self, nome, email, senha) -> None:
        if not nome or nome == '':
            raise APIException('O nome não deve ser null')
        
        if not senha or senha == '':
            raise APIException('A senha não deve ser null')
                
        if not email:
            email = None
        
        usuario = Usuario
        if usuario.objects.filter(nome=nome).exists():
            raise APIException('Este nome já existe')
        
        senha_hashed = make_password(senha)
        
        criar_usuario = usuario.objects.create(
            nome=nome,
            email=email,
            password= senha_hashed,
        )
        
        return criar_usuario