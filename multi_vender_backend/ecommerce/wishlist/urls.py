from django.urls import path

from .views import (
    AddWishlistView,
    WishlistListView,
    RemoveWishlistView
)

urlpatterns = [

    path(
        'add/',
        AddWishlistView.as_view()
    ),

    path(
        'list/',
        WishlistListView.as_view()
    ),

    path(
        'remove/<int:pk>/',
        RemoveWishlistView.as_view()
    ),
]