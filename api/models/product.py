import uuid
import os

from django.db import models
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO 

from .base import Base


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]

    filename = "%s_%s.%s" % ('product', uuid.uuid3(uuid.NAMESPACE_DNS, instance.name), ext)
    return os.path.join('products/normal', filename)

class Product(Base):
    name = models.CharField(max_length=255)
    price_in_cents = models.IntegerField()
    quantity = models.IntegerField(default=0)
    image = models.ImageField(default=None, null=True, blank=True, upload_to=get_file_path)
    thumbnail = models.ImageField(default=None, blank=True, null=True , editable=False)
    category = models.ForeignKey('api.Category', on_delete=models.SET_NULL, default=None, blank=True, null=True)
    
    def save(self, *args ,**kwargs):
      if self.image:     
        thumbnail_size = 120, 120
        image = Image.open(self.image)
        image.thumbnail(thumbnail_size, Image.LANCZOS)
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg', '.webp']:
          FTYPE = 'JPEG'
        elif thumb_extension == '.png':
          FTYPE = 'PNG'
        else:
          return False 

        data_img = BytesIO()
        image.save(data_img, FTYPE)
        data_img.seek(0)
        thumb_filename = os.path.join('products/thumb', thumb_filename)
        self.thumbnail.save(thumb_filename, ContentFile(data_img.read()), save=False)
        data_img.close()
  
      super(Product, self).save(*args , **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    def __str__(self):
        return "Product"
