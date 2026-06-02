from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from .models import Cart
from .serializers import CartSerializer
from rest_framework.generics import ListAPIView
from accounts.permissions import IsCustomer
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class AddToCartView(CreateAPIView):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def perform_create(self, serializer):

        serializer.save(
            customer=self.request.user
        )

class CartListView(ListAPIView):

    serializer_class = CartSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get_queryset(self):

        return Cart.objects.filter(
            customer=self.request.user
        )

class UpdateCartView(UpdateAPIView):

    serializer_class = CartSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get_queryset(self):

        return Cart.objects.filter(
            customer=self.request.user
        )

class RemoveCartView(DestroyAPIView):

    serializer_class = CartSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get_queryset(self):

        return Cart.objects.filter(
            customer=self.request.user
        )

class CartTotalView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get(self, request):

        cart_items = Cart.objects.filter(
            customer=request.user
        )

        total = 0

        for item in cart_items:
            total += (
                item.product.price *
                item.quantity
            )

        return Response({
            "total_amount": total
        })