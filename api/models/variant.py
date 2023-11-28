import uuid
import os

from django.db import models
from .base import Base
from PIL import Image
from io import BytesIO


def get_file_path(instance, filename):
  ext = filename.split('.')[-1]

  filename = "%s_%s.%s" % ('product', uuid.uuid3(uuid.NAMESPACE_DNS, instance.name), ext)
  return os.path.join('products/normal', filename)

class Variant(Base):
  name = models.CharField(max_length=255)
  price_in_cents = models.IntegerField(default=0)
  quantity = models.IntegerField(default=0)
  product = models.ForeignKey('api.Product', on_delete=models.CASCADE, default=None, blank=True, null=True)
  
  class Meta:
    verbose_name = 'Variant'
    verbose_name_plural = 'Variants'
    ordering = ['id']

  def __str__(self):
    return "Variant"
