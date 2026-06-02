# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('SELLER', 'SELLER'),
        ('CUSTOMER', 'CUSTOMER'),
    )

    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
class SellerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    shop_name = models.CharField(max_length=100)

    gst_number = models.CharField(max_length=50)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.shop_name

class CustomerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    address = models.TextField()

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    pincode = models.CharField(max_length=10)