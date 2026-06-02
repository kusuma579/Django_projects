from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.generics import DestroyAPIView

from accounts.permissions import IsCustomer


class AddWishlistView(CreateAPIView):

    queryset = Wishlist.objects.all()

    serializer_class = WishlistSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def perform_create(self, serializer):

        serializer.save(
            customer=self.request.user
        )

class WishlistListView(ListAPIView):

    serializer_class = WishlistSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get_queryset(self):

        return Wishlist.objects.filter(
            customer=self.request.user
        )

class RemoveWishlistView(DestroyAPIView):

    serializer_class = WishlistSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get_queryset(self):

        return Wishlist.objects.filter(
            customer=self.request.user
        )