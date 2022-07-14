from itertools import product
from django import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSeralizer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    seralizer = ProductSeralizer(products, many=True)



    return Response(seralizer.data)