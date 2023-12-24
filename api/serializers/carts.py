from rest_framework import serializers
from ..models import Cart, CartItem
from .cart_items import CartItemsSerializer


class CartsSerializer(serializers.ModelSerializer):
  user_id = serializers.IntegerField(read_only=True)
  cart_items = serializers.SerializerMethodField(method_name='getCartItems')
  
  class Meta:
    model = Cart
    fields = ('id', 'user_id', 'cart_items', 'created_at', 'updated_at')

  
  def getCartItems(self, instance):
    cart_items = CartItem.objects.filter(cart_id = instance.id)

    serializer = CartItemsSerializer(cart_items, context={'request': self.context.get('request')}, many=True)
    return serializer.data