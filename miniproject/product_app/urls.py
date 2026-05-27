from django.urls import path
from .views import *
urlpatterns = [
    path('add_product/',add_product),
    path('product_list/',view_all_products),
    path('delete_product/<int:id>/', delete_product),
    path('update_product/<int:id>/',update_product),
    path('add_to_cart/<int:id>/',add_to_cart),
    path('cart/',view_cart),
    path('remove_from_cart/<int:id>/',remove_from_cart),
]
#http://127.0.0.1:8000/product/add_product
