from ..models import Product
from ..serializers import ProductsSerializer
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductsSerializer
