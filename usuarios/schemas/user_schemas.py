from drf_yasg import openapi
from usuarios.serializers import UsuarioSerializer

retrieve_user_schema = {
    'responses': {
        200: openapi.Response('Successful retrieval of user information', UsuarioSerializer),
        404: 'User not found'
    },
    'operation_summary': 'Retrieve user information',
    'operation_description': 'Retrieve information for the currently authenticated user.'
}

update_user_schema = {
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'nome': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'senha': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    'responses': {
        200: 'User updated successfully',
        400: 'Invalid request'
    },
    'operation_summary': 'Update user information',
    'operation_description': 'Update information for a specific user.'
}

delete_user_schema = {
    'responses': {
        200: 'User deleted successfully',
        404: 'User not found'
    },
    'operation_summary': 'Delete user',
    'operation_description': 'Delete a specific user.'
}
