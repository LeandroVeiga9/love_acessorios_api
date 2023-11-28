from rest_framework import serializers
from ..models import Product


class ProductsSerializer(serializers.ModelSerializer):
  category_id = serializers.IntegerField()

  class Meta:
    model = Product
    fields = ('id', 'category_id', 'name', 'created_at', 'updated_at')
