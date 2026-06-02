from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer

from accounts.permissions import IsCustomer

class CheckoutView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def post(self, request):

        cart_items = Cart.objects.filter(
            customer=request.user
        )

        if not cart_items.exists():

            return Response({
                "message": "Cart is empty"
            })

        total = 0

        for item in cart_items:

            total += (
                item.product.price *
                item.quantity
            )

        order = Order.objects.create(
            customer=request.user,
            total_amount=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            item.product.stock -= item.quantity
            item.product.save()

        cart_items.delete()

        return Response({
            "message": "Order Created",
            "order_id": order.id
        })


class OrderHistoryView(ListAPIView):

    serializer_class = OrderSerializer

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def get_queryset(self):

        return Order.objects.filter(
            customer=self.request.user
        ).order_by('-created_at')

class CancelOrderView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsCustomer
    ]

    def put(self, request, pk):

        order = Order.objects.get(
            id=pk,
            customer=request.user
        )

        order.status = 'CANCELLED'
        order.save()

        return Response({
            "message": "Order Cancelled"
        })

class SellerOrdersView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        orders = OrderItem.objects.filter(
            product__seller=request.user
        )

        data = []

        for item in orders:

            data.append({
                "order_id": item.order.id,
                "product": item.product.name,
                "quantity": item.quantity
            })

        return Response(data)