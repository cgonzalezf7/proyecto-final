from django.urls import path
from TiendaEquipo.views import home, redireccion, nuevo_cliente, lista_clientes, busqueda_clientes, modificar_cliente, eliminar_cliente, proveedores, modificar_proveedor, nuevo_producto, inventario, productos, anadir_unidades, modificar_producto, busqueda_productos, eliminar_producto, ventas, eliminar_venta, factura

#Urls utilizadas para las vistas.
urlpatterns = [
    #Nombre de la url, vista que genera, nombre de referencia.
    path('home/', home, name='home'),
    path('', redireccion, name='redirect'),
    path('nuevo-cliente/', nuevo_cliente, name ='nuevo_cliente'),
    path('lista-clientes/', lista_clientes, name='lista_clientes'),
    path('busqueda-clientes/', busqueda_clientes, name="busqueda_clientes"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name='eliminar_cliente'),
    path('proveedores/', proveedores, name="proveedores"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('nuevo-producto/', nuevo_producto, name="nuevo_producto"),
    path('inventario/', inventario, name="inventario"),
    path('productos/', productos, name="productos"),
    path('anadir-unidades/<id>/', anadir_unidades, name='anadir_unidades'),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('busqueda-productos/', busqueda_productos, name="busqueda_productos"),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    path('ventas/', ventas, name="ventas"),
    path('eliminar-venta/<id>/', eliminar_venta, name='eliminar_venta'),
    path('factura/<id>/', factura, name="factura"),
]