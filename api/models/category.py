from django.db import models
from .base import Base

class Category(Base):
  name = models.CharField(max_length=255)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'
    ordering = ['id']

  def __str__(self):
    return "Category"
