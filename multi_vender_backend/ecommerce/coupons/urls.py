from django.urls import path

from .views import (
    CreateCouponView,
    ApplyCouponView
)

urlpatterns = [

    path(
        'create/',
        CreateCouponView.as_view()
    ),

    path(
        'apply/',
        ApplyCouponView.as_view()
    ),
]