from django.urls import path

from .views import (
    AddToCartView,
    CartListView,
    UpdateCartView,
    RemoveCartView,
    CartTotalView
)

urlpatterns = [

    path(
        'add/',
        AddToCartView.as_view()
    ),

    path(
        'list/',
        CartListView.as_view()
    ),

    path(
        'update/<int:pk>/',
        UpdateCartView.as_view()
    ),

    path(
        'remove/<int:pk>/',
        RemoveCartView.as_view()
    ),

    path(
        'total/',
        CartTotalView.as_view()
    ),
]