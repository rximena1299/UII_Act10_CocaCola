# app_producto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_productos, name='index_productos'), # Cambiado views.index a views.index_productos y el nombre de la URL
    # Añade tus otras rutas de producto aquí, asegurándote de que los nombres de las vistas y URLs coincidan
    path('add/', views.add_producto, name='add_producto'),
    path('edit/<int:id>/', views.edit_producto, name='edit_producto'),
    path('delete/<int:id>/', views.delete_producto, name='delete_producto'),
    # Si vas a usar la vista de detalle
    # path('view/<int:id>/', views.view_producto, name='view_producto'),
]