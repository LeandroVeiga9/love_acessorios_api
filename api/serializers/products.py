from rest_framework import serializers
from ..models import Product, Variant

class ProductsSerializer(serializers.ModelSerializer):
  category_id = serializers.IntegerField()
  cheaper_variant_id = serializers.SerializerMethodField(method_name='getVariant')
  price = serializers.SerializerMethodField(method_name='getPrice')

  class Meta:
    model = Product
    fields = ('id', 'category_id', 'name', 'cheaper_variant_id', 'price', 'created_at', 'updated_at')

  def getVariant(self, instance):
    variants = Variant.objects.filter(product_id = instance.id)
    
    if variants:
      prices = [variant.price_in_cents for variant in variants]
      min_price = min(prices)
      id = variants.filter(price_in_cents = min_price).first().id
    else:
      id = None
  
    return id
  
  def getPrice(self, instance):
    variant_id = self.getVariant(instance)
    
    if variant_id:
      return Variant.objects.get(pk=variant_id).price_in_cents
    
    return None