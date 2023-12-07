from django.db import models
from .base import Base

from .product import Product

class Cart(Base):
  user = models.ForeignKey('api.UserAccount', on_delete=models.CASCADE, default=None, blank=True, null=True)
  products = models.ManyToManyField(Product)
 

  class Meta:
    verbose_name = 'Cart'
    verbose_name_plural = 'Carts'
    ordering = ['id']

  def __str__(self):
    return "Cart"
