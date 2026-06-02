from django.urls import path
from .views import (
    InventoryDashboardView,
    UpdateStockView,
    LowStockProductsView
)
from .views import *

urlpatterns = [

    path(
        'add-product/',
        AddProductView.as_view(),
        name='add-product'
    ),
    path(
        'my-products/',
        SellerProductsView.as_view()
    ),
    path(
        'update-product/<int:pk>/',
        UpdateProductView.as_view()
    ),
    path(
        'delete-product/<int:pk>/',
        DeleteProductView.as_view()
    ),
    path(
        'approved-products/',
        ApprovedProductsView.as_view()
    ),
    path(
        'inventory/',
        InventoryDashboardView.as_view()
    ),

    path(
        'update-stock/<int:product_id>/',
        UpdateStockView.as_view()
    ),

    path(
        'low-stock/',
        LowStockProductsView.as_view()
    ),
]
