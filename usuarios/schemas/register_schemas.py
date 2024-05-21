from drf_yasg import openapi
from usuarios.serializers import UsuarioSerializer
from drf_yasg.utils import swagger_auto_schema

register_post = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['nome', 'email', 'senha'],
        properties={
            'nome': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'senha': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    responses={
        200: openapi.Response('Successful registration', UsuarioSerializer),
        400: 'Invalid request'
    },
    operation_summary='Register a new user',
    operation_description='Register a new user with their name, email, and password.'
)
