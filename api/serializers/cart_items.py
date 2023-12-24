from rest_framework import serializers
from ..models import CartItem
from .variants import VariantsSerializer

class CartItemsSerializer(serializers.ModelSerializer):
  variant = VariantsSerializer(read_only=True)
  cart_id = serializers.IntegerField(read_only=True)
  
  class Meta:
    model = CartItem
    fields = ('id', 'price_in_cents', 'quantity', 'cart_id', 'variant', 'created_at', 'updated_at')
