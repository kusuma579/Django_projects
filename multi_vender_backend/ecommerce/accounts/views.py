from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import *
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

class RegisterView(CreateAPIView):

    serializer_class = RegisterSerializer


class SellerDashboard(APIView):

    permission_classes = [IsSeller]

    def get(self, request):

        return Response({
            "message": "Welcome Seller"
        })
class CustomerDashboard(APIView):

    permission_classes = [IsCustomer]

    def get(self, request):

        return Response({
            "message": "Welcome Customer"
        })

class AdminDashboard(APIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({
            "message": "Welcome Admin",
            "username": request.user.username,
            "role": request.user.role
        })
