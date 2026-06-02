from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from accounts.permissions import IsSeller
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class AddProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]
    def perform_create(self, serializer):

        serializer.save(
            seller=self.request.user
        )

class SellerProductsView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]
    def get_queryset(self):
        return Product.objects.filter(
            seller=self.request.user
        )

class UpdateProductView(UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]
    def get_queryset(self):
        return Product.objects.filter(
            seller=self.request.user
        )

class DeleteProductView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]
    def get_queryset(self):
        return Product.objects.filter(
            seller=self.request.user
        )


class ApprovedProductsView(ListAPIView):

    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Product.objects.filter(
            is_approved=True
        )

class InventoryDashboardView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]

    def get(self, request):

        seller = request.user.sellerprofile

        products = Product.objects.filter(
            seller=seller
        )

        total_products = products.count()

        out_of_stock = products.filter(
            stock=0
        ).count()

        low_stock = products.filter(
            stock__lte=5,
            stock__gt=0
        ).count()

        return Response({

            "total_products": total_products,

            "out_of_stock": out_of_stock,

            "low_stock": low_stock
        })
class UpdateStockView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]

    def put(self, request, product_id):

        product = Product.objects.get(
            id=product_id
        )

        product.stock = request.data.get(
            "stock"
        )

        product.save()

        return Response({
            "message": "Stock Updated",
            "current_stock": product.stock
        })

class LowStockProductsView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsSeller
    ]

    def get(self, request):

        seller = request.user.sellerprofile

        products = Product.objects.filter(
            seller=seller,
            stock__lte=5
        )

        data = []

        for product in products:

            data.append({
                "id": product.id,
                "name": product.name,
                "stock": product.stock
            })

        return Response(data)