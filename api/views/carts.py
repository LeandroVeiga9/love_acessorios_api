from ..models import Cart, CartItem, Variant
from ..serializers import CartsSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..permissions import CartsPermissions

class CartsViewSet(viewsets.ModelViewSet):
  queryset = Cart.objects.all()
  serializer_class = CartsSerializer
  permission_classes = (CartsPermissions,)
  
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    cart = Cart.objects.get(id=response.data['id'])
    
    if not request.user.is_anonymous:
      cart.user = request.user
    
    for id in request.data['variants']:
      # separete this "try" in a separeted helper (add item on cart)
      try:
        variant = Variant.objects.get(pk=id)
        CartItem(
          price_in_cents=variant.price_in_cents,
          variant_id=variant.id,
          cart_id=cart.id
        ).save()
      except:
        cart.delete()
        message = f"Variant with id {id} doesn't exists"
        return Response({"message": message}, status=400)
      
    cart.save()
    
    return Response(CartsSerializer(cart, context={'request': request}).data, status=200)
  
  @action(detail=True, methods=['post'])
  def add_item(self, request, pk=None):
    cart = self.get_object()
    
    try:
      variant = Variant.objects.get(pk=request.data['variant_id'])
      cart_item = CartItem.objects.filter(variant_id=100, cart_id=cart.id)
      
      if cart_item:
        cart_item.quantity = cart_item.quantity + request.data['quantity']
        cart_item.save()
      else:
        if request.data['quantity'] > variant.quantity:
          return Response({"message": f"You can't add more than {variant.quantity} items on the cart"}, status=400)
        else:
          CartItem(
            price_in_cents=variant.price_in_cents,
            variant_id=variant.id,
            quantity=request.data['quantity'],
            cart_id=cart.id
          ).save()
    except:
      message = f"Variant with id {request.data['variant_id']} doesn't exists"
      return Response({"message": message}, status=400)
    
    return Response({'message': 'Product added to cart'}, status=200)
  
  @action(detail=True, methods=['post'])
  def checkout(self, request, pk=None):
    cart = self.get_object()
    
    # payment
    
    cart_items = CartItem.objects.filter(cart_id = cart.id)
    for cart_item in cart_items:
      cart_item.variant.quantity = (cart_item.variant.quantity - cart_item.quantity)
      cart_item.variant.save()
    
    cart.status = "FINISHED"
    cart.save()

    
    return Response({}, status=200)