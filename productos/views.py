from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria


def formato_clp(valor):
    try:
        numero = int(valor)
        return f"{numero:,}".replace(",", ".")
    except (ValueError, TypeError):
        return valor


def agregar_precios_formateados(productos):
    for producto in productos:
        producto.precio_formateado = formato_clp(producto.precio)
    return productos


def home(request):
    productos_destacados = list(
        Producto.objects.filter(
            activo=True,
            destacado=True
        )[:6]
    )

    agregar_precios_formateados(productos_destacados)

    return render(request, 'productos/home.html', {
        'productos_destacados': productos_destacados
    })


def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    productos = list(productos)
    agregar_precios_formateados(productos)

    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'categorias': categorias,
    })


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)
    producto.precio_formateado = formato_clp(producto.precio)

    return render(request, 'productos/detalle.html', {
        'producto': producto
    })