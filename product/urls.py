from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_products, name='get_products'),
    path('create/', create_product, name='create_product'),
    path('delete/<int:pk>/', delete_product, name = 'delete_product'),
    path('get/<int:pk>/', get_one_product, name = 'get_one_product'),
    path('update/<int:pk>/', update_product)
]