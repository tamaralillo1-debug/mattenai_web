# Mattenai Web - Ecommerce Django

## Autora

Tamara Noemí Lillo Martínez

## URL del repositorio GitHub

Repositorio público:  
https://github.com/tamaralillo1-debug/mattenai_web

## Objetivo de la aplicación

El objetivo de esta aplicación es desarrollar un ecommerce funcional para la tienda Mattenai, permitiendo a los usuarios navegar por un catálogo de joyas y accesorios, revisar el detalle de los productos, agregar productos al carrito, validar stock disponible y confirmar pedidos asociados a un usuario autenticado.

El proyecto fue desarrollado como entrega final del Módulo 8, integrando autenticación, catálogo persistente, carrito de compras, confirmación de pedidos y administración de productos mediante Django Admin.

## Descripción del proyecto

Mattenai es una tienda online de joyas y accesorios con productos desde $4.990.  
La aplicación permite gestionar productos desde el panel administrador y simular un flujo completo de compra desde el catálogo hasta la confirmación del pedido.

## Funcionalidades principales

- Inicio de sesión para cliente.
- Acceso de administrador.
- Catálogo de productos desde base de datos.
- Detalle de producto.
- Carrito de compras.
- Agregar productos al carrito.
- Quitar productos del carrito.
- Actualizar cantidades.
- Validación de stock disponible.
- Confirmación de compra.
- Registro de pedido asociado al usuario autenticado.
- Administración de categorías y productos desde Django Admin.
- Administración de pedidos desde Django Admin.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- Bootstrap
- HTML
- CSS

## Instalación y ejecución local

1. Clonar el repositorio:

```powershell
git clone https://github.com/tamaralillo1-debug/mattenai_web
Ingresar a la carpeta del proyecto:
cd mattenai_web
Crear entorno virtual:
python -m venv venv
Activar entorno virtual:
.\venv\Scripts\Activate.ps1
Instalar dependencias:
pip install -r requirements.txt
Aplicar migraciones:
python manage.py migrate
Ejecutar servidor local:
python manage.py runserver
Abrir en el navegador:
http://127.0.0.1:8000/
Rutas principales
Ruta	Descripción
/	Página de inicio
/catalogo/	Catálogo de productos
/producto/<id>/	Detalle de producto
/carrito/	Carrito de compras
/pedidos/confirmar/	Confirmación de pedido
/accounts/login/	Inicio de sesión
/admin/	Panel de administración
Credenciales de prueba
Administrador
Usuario: Admin
Contraseña: 123456
Cliente
Usuario: Cliente
Contraseña: Joyas$Regalo2026
Flujo principal probado
Cliente ingresa al catálogo.
Revisa el detalle del producto.
Agrega producto al carrito.
Actualiza cantidad o elimina producto.
El sistema valida stock disponible.
Cliente inicia sesión.
Confirma compra.
Se registra el pedido en la base de datos.
Administrador revisa el pedido en Django Admin.
Estado del proyecto

Proyecto funcional en entorno local para entrega final de ecommerce.