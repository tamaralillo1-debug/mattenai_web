from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria


def home(request):
    productos_destacados = Producto.objects.filter(
        activo=True,
        destacado=True
    )[:6]

    return render(request, 'productos/home.html', {
        'productos_destacados': productos_destacados
    })


def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    return render(request, 'productos/catalogo.html', {
        'productos': productos,
        'categorias': categorias,
    })


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, activo=True)

    return render(request, 'productos/detalle.html', {
        'producto': producto
    })