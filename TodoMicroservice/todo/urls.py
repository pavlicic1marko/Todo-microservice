from django.urls import path
from . import views

urlpatterns = [
    path('routes', views.getRoutes, name='routes'),
    path('todo/products', views.getProducts, name='products'),
    path('todo/products/<str:pk>', views.getProductsById, name='products'),
    path('create', views.createTodo, name='create'),

]