from django.db import models

# Create your models here.
class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_type = models.CharField(max_length=100)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_quantity = models.IntegerField()

class CartModel(models.Model):
     product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)