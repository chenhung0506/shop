from django.db import models

class Product(models.Model):
    product_id = models.AutoField(auto_created=True, primary_key=True)
    stock_pcs = models.IntegerField()
    price = models.IntegerField()
    shop_id = models.CharField(max_length=100)
    vip = models.BooleanField(default=False)

class Order(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True)
    product_id = models.ForeignKey('Product', on_delete=models.PROTECT)
    qty = models.IntegerField()
    price = models.IntegerField()
    shop_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
