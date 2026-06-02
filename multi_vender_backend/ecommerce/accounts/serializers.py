from rest_framework import serializers
from .models import User, SellerProfile, CustomerProfile

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone',
            'password',
            'role'
        ]

    def create(self, validated_data):

        password = validated_data.pop('password')

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        if user.role == 'SELLER':

            SellerProfile.objects.create(
                user=user,
                shop_name='New Shop',
                gst_number='PENDING'
            )

        elif user.role == 'CUSTOMER':

            CustomerProfile.objects.create(
                user=user,
                address='',
                city=''
            )

        return user