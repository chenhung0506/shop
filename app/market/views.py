from django.shortcuts import render
from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from market.serializers import ProductSerializer 
from market.serializers import OrderSerializer 
from market.models import Product
from market.models import Order
import logging
import json
    
log = logging.getLogger(__name__)

class Resource(GenericAPIView):
  def get(self, request):
    return render(request, 'index.html')

class StaticResource(GenericAPIView):
  def get(self, request, *args, **krgs):
    log.info(args[0])
    return render(request, args[0])

# curl -XPOST  localhost:8000/products -H 'content-type: application/json' -d '{"stock_pcs": 5, "price":123, "shop_id":"shop_id","vip":true}' | jq

class Product(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def delete(self, request, *args, **krgs):
        log.info("success::::::::::::")
        data = request.data
        log.info(data)
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.delete()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
    def get(self, request, *args, **krgs):
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)
        data = serializer.data
        log.info(data)
        return JsonResponse({"data":data}, safe=False)
    def post(self, request, *args, **krgs):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                serializer.save()
            data = serializer.data
        except Exception as e:
            data = {'error': str(e)}
        return JsonResponse(data)

# curl -XPOST  localhost:8000/orders -H 'content-type: application/json' -d '{"product_id": 1, "qty": 1,"price":123, "shop_id":"shop_id", "customer_id":"123"}' | jq

class Order(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, *args, **krgs):
        products = Product().get(request, None, None)
        products = json.loads(products.content)
        log.info(products)
        orders = self.get_queryset()
        serializer = self.serializer_class(orders, many=True)
        data = serializer.data
        return JsonResponse({"data":data}, safe=False)
    def post(self, request, *args, **krgs):
        data = request.data
        log.info(data)
        try:
            serializer = self.serializer_class(data=data)
            log.info(1)
            serializer.is_valid(raise_exception=True)
            log.info(2)
            with transaction.atomic():
                log.info(3)
                serializer.save()
            log.info(4)
            data = serializer.data
        except Exception as e:
            log.info(e)
            data = {'error': str(e)}
        return JsonResponse(data)