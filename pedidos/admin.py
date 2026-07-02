from django.contrib import admin
from .models import Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ("producto", "cantidad", "precio_unitario", "subtotal")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "fecha", "total", "estado")
    list_filter = ("estado", "fecha")
    search_fields = ("usuario__username", "usuario__email")
    inlines = [ItemPedidoInline]


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "producto", "cantidad", "precio_unitario", "subtotal")