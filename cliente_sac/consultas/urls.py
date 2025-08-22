from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('exportar/<int:cliente_id>/', views.exportar_cliente_csv, name='exportar_csv'),
]