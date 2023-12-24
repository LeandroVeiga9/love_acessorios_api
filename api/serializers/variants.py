from rest_framework import serializers
from ..models import Variant


class VariantsSerializer(serializers.ModelSerializer):
  product_id = serializers.IntegerField()
  
  class Meta:
    model = Variant
    fields = ('id', 'name', 'quantity', 'price_in_cents', 'product_id', 'created_at', 'updated_at')
