from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Tax
from .serializers import TaxSerializer

from accounts.permissions import IsAdmin
from orders.models import Order


class CreateTaxView(CreateAPIView):

    queryset = Tax.objects.all()

    serializer_class = TaxSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]


class GenerateBillView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, order_id):

        order = Order.objects.get(id=order_id)

        tax = Tax.objects.get(is_active=True)

        gst_amount = (
            order.total_amount *
            tax.tax_percentage
        ) / 100

        cgst = gst_amount / 2

        sgst = gst_amount / 2

        final_amount = (
            order.total_amount +
            gst_amount
        )

        return Response({

            "order_id": order.id,

            "order_amount": order.total_amount,

            "gst_percentage": tax.tax_percentage,

            "cgst": cgst,

            "sgst": sgst,

            "gst_total": gst_amount,

            "final_amount": final_amount
        })