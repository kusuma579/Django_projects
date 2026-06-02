from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [

    path(
        'register/',
        RegisterView.as_view()
    ),

    path(
        'login/',
        TokenObtainPairView.as_view()
    ),

    path(
        'refresh/',
        TokenRefreshView.as_view()
    ),

    path(
        'seller-dashboard/',
        SellerDashboard.as_view()
    ),

    path(
        'customer-dashboard/',
        CustomerDashboard.as_view()
    ),

    path(
        'admin-dashboard/',
        AdminDashboard.as_view(),
        name='admin-dashboard'
    ),
]