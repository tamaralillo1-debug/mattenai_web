from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from productos.models import Producto
from .models import Pedido, ItemPedido


@login_required
def confirmar_pedido(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')

    # Validación de stock antes de crear pedido
    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)

        if cantidad > producto.stock:
            messages.error(
                request,
                f"No hay stock suficiente para {producto.nombre}. Stock disponible: {producto.stock}."
            )
            return redirect('ver_carrito')

    pedido = Pedido.objects.create(
        usuario=request.user,
        total=Decimal('0'),
        estado='pendiente'
    )

    total = Decimal('0')

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal

        ItemPedido.objects.create(
            pedido=pedido,
            producto=producto,
            cantidad=cantidad,
            precio_unitario=producto.precio,
            subtotal=subtotal
        )

        producto.stock -= cantidad
        producto.save()

    pedido.total = total
    pedido.save()

    request.session['carrito'] = {}
    request.session.modified = True

    messages.success(request, "Pedido registrado correctamente.")

    return render(request, 'pedidos/confirmacion.html', {
        'pedido': pedido
    })