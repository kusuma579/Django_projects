from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin
from accounts.models import SellerProfile
from .serializers import SellerApprovalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from .serializers import ProductApprovalSerializer

class SellerListView(ListAPIView):

    queryset = SellerProfile.objects.all()

    serializer_class = SellerApprovalSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

class ApproveSellerView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def put(self, request, pk):

        seller = get_object_or_404(
            SellerProfile,
            pk=pk
        )

        seller.is_approved = True

        seller.save()

        return Response({
            "message": "Seller Approved"
        })

class ProductListView(ListAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductApprovalSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

class ApproveProductView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]
    def put(self, request, pk):
        product = get_object_or_404(
            Product,
            pk=pk
        )
        product.is_approved = True
        product.save()
        return Response({
            "message": "Product Approved"
        })