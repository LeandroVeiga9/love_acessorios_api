from django.db import models
from .base import Base

class CartItem(Base):
  price_in_cents = models.IntegerField(default=0)
  quantity = models.IntegerField(default=1)
  variant = models.ForeignKey('api.Variant', on_delete=models.SET_NULL, default=None, blank=True, null=True)
  cart = models.ForeignKey('api.Cart', on_delete=models.CASCADE)

  class Meta:
    verbose_name = 'CartItem'
    verbose_name_plural = 'CartItems'
    ordering = ['id']

  def __str__(self):
    return "CartItem"
