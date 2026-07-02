from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('procesar/', views.procesar_carrito, name='procesar_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('actualizar/<int:producto_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('quitar/<int:producto_id>/', views.quitar_carrito, name='quitar_carrito'),
]