from drf_yasg import openapi
from itens.serializers import ItemSerializer
from drf_yasg.utils import swagger_auto_schema

list_items_get = swagger_auto_schema(
    responses={
        200: openapi.Response('List of items', ItemSerializer(many=True)),
    },
    operation_summary='List items',
    operation_description='Get a list of all items.'
)

create_item_post = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['nome', 'preco'],
        properties={
            'nome': openapi.Schema(type=openapi.TYPE_STRING),
            'preco': openapi.Schema(type=openapi.TYPE_NUMBER),
        }
    ),
    responses={
        201: openapi.Response('Item created successfully', ItemSerializer),
        400: 'Invalid request'
    },
    operation_summary='Create item',
    operation_description='Create a new item.'
)

retrieve_item_get = swagger_auto_schema(
    responses={
        200: openapi.Response('Item details', ItemSerializer),
        404: 'Item not found'
    },
    operation_summary='Retrieve item details',
    operation_description='Retrieve details for a specific item.'
)

update_item_put = swagger_auto_schema(
    responses={
        200: 'Item updated successfully',
        400: 'Invalid request'
    },
    operation_summary='Update item details',
    operation_description='Update details for a specific item.'
)

delete_item_delete = swagger_auto_schema(
    responses={
        200: 'Item deleted successfully',
        404: 'Item not found'
    },
    operation_summary='Delete item',
    operation_description='Delete a specific item.'
)
