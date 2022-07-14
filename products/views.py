from itertools import product
from urllib import response
from django import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSeralizer
from products import serializers

@api_view(['GET', 'POST'])
def product_list(request):
   
   
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSeralizer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSeralizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
            