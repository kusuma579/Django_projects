from django.db import models

# Create your models here.
from django.db import models


class Tax(models.Model):

    tax_name = models.CharField(
        max_length=50
    )

    tax_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.tax_name