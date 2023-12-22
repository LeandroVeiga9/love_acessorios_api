from ..models import CartItem
from ..serializers import CartItemsSerializer
from rest_framework import viewsets


class CartItemsViewSet(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemsSerializer
