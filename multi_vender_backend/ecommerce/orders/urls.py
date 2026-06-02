from django.urls import path

from .views import (
    CheckoutView,
    OrderHistoryView,
    CancelOrderView,
    SellerOrdersView
)

urlpatterns = [

    path(
        'checkout/',
        CheckoutView.as_view()
    ),

    path(
        'history/',
        OrderHistoryView.as_view()
    ),

    path(
        'cancel/<int:pk>/',
        CancelOrderView.as_view()
    ),

    path(
        'seller-orders/',
        SellerOrdersView.as_view()
    ),
]