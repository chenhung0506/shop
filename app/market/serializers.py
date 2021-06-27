from market.models import Product
from market.models import Order
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
     class Meta:
         model = Order
         fields = '__all__'