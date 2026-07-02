from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto


def formato_clp(valor):
    try:
        numero = int(valor)
        return f"{numero:,}".replace(",", ".")
    except (ValueError, TypeError):
        return valor


def obtener_carrito(request):
    return request.session.get('carrito', {})


def guardar_carrito(request, carrito):
    request.session['carrito'] = carrito
    request.session.modified = True


def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)

    if producto.stock <= 0:
        messages.error(request, f"{producto.nombre} está agotado.")
        return redirect('catalogo')

    carrito = obtener_carrito(request)
    producto_id_str = str(producto.id)

    cantidad_actual = carrito.get(producto_id_str, 0)
    nueva_cantidad = cantidad_actual + 1

    if nueva_cantidad > producto.stock:
        messages.error(
            request,
            f"No puedes agregar más de {producto.stock} unidades de {producto.nombre}. Stock disponible: {producto.stock}."
        )
        return redirect('ver_carrito')

    carrito[producto_id_str] = nueva_cantidad
    guardar_carrito(request, carrito)

    messages.success(request, f"{producto.nombre} fue agregado al carrito.")
    return redirect('ver_carrito')


def ver_carrito(request):
    carrito = obtener_carrito(request)
    items = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal

        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
            'precio_formateado': formato_clp(producto.precio),
            'subtotal_formateado': formato_clp(subtotal),
        })

    return render(request, 'carrito/carrito.html', {
        'items': items,
        'total': total,
        'total_formateado': formato_clp(total),
    })


def procesar_carrito(request):
    if request.method != 'POST':
        return redirect('ver_carrito')

    carrito = obtener_carrito(request)

    if not carrito:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('ver_carrito')

    accion = request.POST.get('accion')
    nuevo_carrito = {}
    hay_error = False

    for producto_id, cantidad_actual in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id, activo=True)

        try:
            cantidad = int(request.POST.get(f'cantidad_{producto_id}', cantidad_actual))
        except ValueError:
            cantidad = cantidad_actual

        if cantidad <= 0:
            messages.error(request, f"La cantidad de {producto.nombre} debe ser mayor a 0.")
            nuevo_carrito[producto_id] = cantidad_actual
            hay_error = True
            continue

        if cantidad > producto.stock:
            messages.error(
                request,
                f"No puedes comprar {cantidad} unidades de {producto.nombre}. El máximo disponible es {producto.stock}."
            )
            nuevo_carrito[producto_id] = cantidad_actual
            hay_error = True
            continue

        nuevo_carrito[producto_id] = cantidad

    guardar_carrito(request, nuevo_carrito)

    if hay_error:
        return redirect('ver_carrito')

    if accion == 'confirmar':
        return redirect('confirmar_pedido')

    messages.success(request, "Carrito actualizado correctamente.")
    return redirect('ver_carrito')


def actualizar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)

    if request.method == 'POST':
        try:
            cantidad = int(request.POST.get('cantidad', 1))
        except ValueError:
            cantidad = 1

        carrito = obtener_carrito(request)
        producto_id_str = str(producto.id)

        if cantidad <= 0:
            carrito.pop(producto_id_str, None)
            messages.success(request, f"{producto.nombre} fue eliminado del carrito.")

        elif cantidad > producto.stock:
            messages.error(
                request,
                f"No puedes comprar {cantidad} unidades de {producto.nombre}. El máximo disponible es {producto.stock}."
            )

        else:
            carrito[producto_id_str] = cantidad
            messages.success(request, "Carrito actualizado correctamente.")

        guardar_carrito(request, carrito)

    return redirect('ver_carrito')


def quitar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    carrito = obtener_carrito(request)
    producto_id_str = str(producto.id)

    carrito.pop(producto_id_str, None)
    guardar_carrito(request, carrito)

    messages.success(request, f"{producto.nombre} fue eliminado del carrito.")
    return redirect('ver_carrito')