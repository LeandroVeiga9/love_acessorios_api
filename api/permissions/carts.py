from rest_framework import permissions
from ..models import Cart

class CartsPermissions(permissions.BasePermission):
  def has_permission(self, request, view):
    if view.action == 'add_item' or view.action == 'update' or view.action == "destroy" or view.action == 'retrieve':
      cart = Cart.objects.get(id=view.kwargs.get('pk'))
      if not request.user or request.user.is_anonymous:
        print("aqui")
        if cart.user == None:
          return True
        return False
      else:
        if request.user == cart.user:
          return True
        return False

    return False