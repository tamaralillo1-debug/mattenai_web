from django.urls import path
from . import views

urlpatterns = [
    path('confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
]