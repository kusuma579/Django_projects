from django.db import models

# Create your models here.
from django.db import models


class Coupon(models.Model):

    DISCOUNT_TYPES = [
        ('PERCENTAGE', 'Percentage'),
        ('FLAT', 'Flat'),
    ]

    code = models.CharField(
        max_length=50,
        unique=True
    )

    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPES
    )

    discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    min_purchase = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    expiry_date = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.code