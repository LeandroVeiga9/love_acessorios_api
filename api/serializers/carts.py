from rest_framework import serializers
from ..models import Cart
from ..serializers import UserSerializer, ProductsSerializer


class CartsSerializer(serializers.ModelSerializer):
  # user = serializers.SerializerMethodField(method_name="get_user")
  user_id = serializers.IntegerField(read_only=True)
  products = ProductsSerializer(read_only=True, many=True)
  
  class Meta:
    model = Cart
    fields = ('id', 'user_id', 'products', 'created_at', 'updated_at')
