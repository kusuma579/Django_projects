from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Coupon
from .serializers import CouponSerializer

from accounts.permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import date
class CreateCouponView(CreateAPIView):

    queryset = Coupon.objects.all()

    serializer_class = CouponSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

class ApplyCouponView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        code = request.data.get('code')
        amount = float(request.data.get('amount'))

        try:

            coupon = Coupon.objects.get(
                code=code,
                is_active=True
            )

        except Coupon.DoesNotExist:

            return Response({
                "message": "Invalid Coupon"
            })

        if coupon.expiry_date < date.today():

            return Response({
                "message": "Coupon Expired"
            })

        if amount < coupon.min_purchase:

            return Response({
                "message": "Minimum Purchase Not Reached"
            })

        if coupon.discount_type == 'PERCENTAGE':

            discount = (
                amount *
                float(coupon.discount_value)
            ) / 100

        else:

            discount = float(
                coupon.discount_value
            )

        final_amount = amount - discount

        return Response({

            "coupon": coupon.code,

            "original_amount": amount,

            "discount": discount,

            "final_amount": final_amount
        })