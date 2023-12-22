from rest_framework import serializers
from ..models import CartItem


class CartItemsSerializer(serializers.ModelSerializer):
  product_id = serializers.IntegerField(read_only=True)
  cart_id = serializers.IntegerField(read_only=True)
  
  class Meta:
    model = CartItem
    fields = ('id', 'price_in_cents', 'quantity', 'cart_id', 'product_id', 'created_at', 'updated_at')
