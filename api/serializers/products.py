from rest_framework import serializers
from ..models import Product, Variant

class ProductsSerializer(serializers.ModelSerializer):
  category_id = serializers.IntegerField()
  price = serializers.SerializerMethodField(method_name='getPrice')

  class Meta:
    model = Product
    fields = ('id', 'category_id', 'name', 'price', 'created_at', 'updated_at')

  def getPrice(self, instance):
    variants = Variant.objects.filter(product_id = instance.id)
    
    if variants:
      prices = [variant.price_in_cents for variant in variants]
      min_price = min(prices)
    else:
      min_price = 0
      
    return min_price