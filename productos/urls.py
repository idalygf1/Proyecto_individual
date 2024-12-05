from django.urls import path
from . import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login', auth_views.LoginView.as_view(template_name='productos/login.html'), name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('comprar/', views.realizar_compra, name='realizar_compra'),  
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    path('pedidos/', views.pedidos, name='pedidos')
]

