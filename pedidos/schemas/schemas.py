from drf_yasg import openapi
from pedidos.serializers import PedidoSerializer
from drf_yasg.utils import swagger_auto_schema

list_orders_get = swagger_auto_schema(
    responses={
        200: openapi.Response('List of user\'s orders', PedidoSerializer(many=True)),
    },
    operation_summary='List user orders',
    operation_description='Get a list of orders for the currently authenticated user.'
)

create_order_post = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['itens'],
        properties={
            'itens': openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'item': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'quantidade': openapi.Schema(type=openapi.TYPE_INTEGER),
                    }
                )
            )
        }
    ),
    responses={
        201: openapi.Response('Order created successfully', PedidoSerializer),
        400: 'Invalid request'
    },
    operation_summary='Create a new order',
    operation_description='Create a new order for the currently authenticated user.'
)

retrieve_order_get = swagger_auto_schema(
    responses={
        200: openapi.Response('Order details', PedidoSerializer),
        404: 'Order not found'
    },
    operation_summary='Retrieve order details',
    operation_description='Retrieve details for a specific order.'
)

update_order_put = swagger_auto_schema(
    responses={
        200: 'Order updated successfully',
        400: 'Invalid request'
    },
    operation_summary='Update order details',
    operation_description='Update details for a specific order.'
)

delete_order_delete = swagger_auto_schema(
    responses={
        204: 'Order deleted successfully',
        404: 'Order not found'
    },
    operation_summary='Delete order',
    operation_description='Delete a specific order.'
)
