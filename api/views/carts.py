from ..models import Cart
from ..serializers import CartsSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class CartsViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartsSerializer
  
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    cart = Cart.objects.get(id=response.data['id'])
    if request.user:
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