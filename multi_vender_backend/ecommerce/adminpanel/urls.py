from django.urls import path

from .views import (
    SellerListView,
    ApproveSellerView,
    ProductListView,
    ApproveProductView
)

urlpatterns = [

    path(
        'sellers/',
        SellerListView.as_view()
    ),

    path(
        'approve-seller/<int:pk>/',
        ApproveSellerView.as_view()
    ),

    path(
        'products/',
        ProductListView.as_view()
    ),

    path(
        'approve-product/<int:pk>/',
        ApproveProductView.as_view()
    ),
]