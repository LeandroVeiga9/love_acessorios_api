import uuid
import os

from django.db import models

from .base import Base


def get_file_path(instance, filename):
  ext = filename.split('.')[-1]

  filename = "%s_%s.%s" % ('product', uuid.uuid3(uuid.NAMESPACE_DNS, instance.name), ext)
  return os.path.join('products/normal', filename)

class Product(Base):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255, default=None, blank=True, null=True)
  quantity = models.IntegerField(default=0)
  category = models.ForeignKey('api.Category', on_delete=models.SET_NULL, default=None, blank=True, null=True)

  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
    ordering = ['id']

  def __str__(self):
    return "Product"
