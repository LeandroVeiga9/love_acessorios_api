from django.db import models


class Base(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

  def update_field(self, field, value):
    current_instance = self
    setattr(current_instance, field, value)
    current_instance.save()
    return current_instance
