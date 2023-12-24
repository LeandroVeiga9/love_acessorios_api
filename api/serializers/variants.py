from rest_framework import serializers
from ..models import Variant
from .products import ProductsSerializer

class VariantsSerializer(serializers.ModelSerializer):
  product = ProductsSerializer(read_only=True)
  
  class Meta:
    model = Variant
    fields = ('id', 'name', 'quantity', 'price_in_cents', 'product', 'thumbnail', 'image', 'created_at', 'updated_at')
