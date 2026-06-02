from rest_framework import serializers

from accounts.models import SellerProfile
from products.models import Product


class SellerApprovalSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerProfile
        fields = '__all__'


class ProductApprovalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'