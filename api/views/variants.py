from ..models import Variant
from ..serializers import VariantsSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..pagination.customPagination import CustomPagination


class VariantsViewSet(viewsets.ModelViewSet):
  queryset = Variant.objects.all()
  serializer_class = VariantsSerializer

  def list(self, request, *args, **kwargs):
    paginator = CustomPagination()
    variants = Variant.objects.all()
    
    if 'product_id' in request.query_params:
      variants = Variant.objects.filter(product_id = request.query_params['product_id'])
    
    page = paginator.paginate_queryset(variants, request)
    serializer = VariantsSerializer(page, many=True, context={'request': self.request})
    return paginator.get_paginated_response(serializer.data)