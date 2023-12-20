from ..models import Product
from ..serializers import ProductsSerializer
from rest_framework import viewsets
from ..pagination.customPagination import CustomPagination


class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductsSerializer
  
  def list(self, request, *args, **kwargs):
    paginator = CustomPagination()
    products = Product.objects.all()
    
    if 'category_id' in request.query_params:
      products = Product.objects.filter(category_id = request.query_params['category_id'])
    
    if 'name' in request.query_params:
      products = products.filter(name__contains = request.query_params['name'])
    
    page = paginator.paginate_queryset(products, request)
    serializer = ProductsSerializer(page, many=True, context={'request': self.request})
    return paginator.get_paginated_response(serializer.data)
