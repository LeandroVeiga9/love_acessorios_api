from django.db import models
from .base import Base

from .product import Product

class Cart(Base):
  CART_STATUS_OPTIONS = [
    ('ACTIVE', 'active'),
    ('FINISHED', 'finished'),
  ]
  user = models.ForeignKey('api.UserAccount', on_delete=models.SET_NULL, default=None, blank=True, null=True)
  total_price = models.IntegerField(default=0)
  status = models.CharField(max_length = 10, choices=CART_STATUS_OPTIONS, default='ACTIVE')

  class Meta:
    verbose_name = 'Cart'
    verbose_name_plural = 'Carts'
    ordering = ['id']

  def __str__(self):
    return "Cart"
