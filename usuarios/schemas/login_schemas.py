from drf_yasg import openapi
from usuarios.serializers import UsuarioSerializer
from drf_yasg.utils import swagger_auto_schema

login_post = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['nome', 'senha'],
        properties={
            'nome': openapi.Schema(type=openapi.TYPE_STRING),
            'senha': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={
        200: openapi.Response('Successful login', UsuarioSerializer),
        400: 'Invalid request'
    },
    operation_summary='Log in a user',
    operation_description='Log in a user with their name and password to obtain access and refresh tokens.'
)
