from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]