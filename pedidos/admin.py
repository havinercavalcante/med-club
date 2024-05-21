from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ['id', 'usuario', 'data_criacao', 'total']
    list_filter = ['usuario']
    search_fields = ['usuario__username', 'id']

admin.site.register(Pedido, PedidoAdmin)
