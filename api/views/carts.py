from ..models import Cart
from ..serializers import CartsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..permissions import CartsPermissions
from rest_framework.permissions import AllowAny

class CartsViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartsSerializer
  permission_classes = (CartsPermissions,)
  
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    cart = Cart.objects.get(id=response.data['id'])
    
    if not request.user.is_anonymous:
      cart.user = request.user
    
    for id in request.data['products']:
      try:
        cart.products.add(id)
      except:
        cart.delete()
        message = f"Product with id {id} doesn't exists"
        return Response({"message": message}, status=400)
      
    cart.save()
    
    return Response(CartsSerializer(cart, context={'request': request}).data, status=200)
  
  # @action(detail=True, methods=['post'], url_path='tags/remove/(?P<tag_pk>[^/.]+)')
  @action(detail=True, methods=['post'])
  def add_item(self, request, pk=None):
    cart = self.get_object()
    cart.products.add(request.data['product_id'])
    
    return Response({'message': 'Product added to cart'}, status=200)