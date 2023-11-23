from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
import os
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

class UserAccountManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
      if not email:
          raise ValueError('Users must have an email address')
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save()
      return user

  def create_superuser(self, email, password, **extra_fields):
      user = self.create_user(
          email,
          password=password,
          **extra_fields
      )
      user.is_staff = True
      user.save(using=self._db)
      return user


def get_file_path(instance, filename):
  ext = filename.split('.')[-1]

  filename = "%s_%s.%s" % ('user', uuid.uuid3(
      uuid.NAMESPACE_DNS, instance.email), ext)
  return os.path.join('users', filename)


class UserAccount(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=255, unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  profile_image = models.ImageField(
    default=None, null=True, blank=True, upload_to=get_file_path)
  profile_image_url = models.URLField(default=None, null=True, blank=True)
  thumbnail = models.ImageField(editable=False , default=None)
  objects = UserAccountManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
  
  
  def save(self, *args ,**kwargs):
    if self.profile_image:     
      thumbnail_size = 120, 120
      image = Image.open(self.profile_image)
      image.thumbnail(thumbnail_size, Image.ANTIALIAS)
      thumb_name, thumb_extension = os.path.splitext(self.profile_image.name)
      thumb_extension = thumb_extension.lower()
      thumb_filename = thumb_name + '_thumb' + thumb_extension

      if thumb_extension in ['.jpg', '.jpeg', '.webp']:
        FTYPE = 'JPEG'
      elif thumb_extension == '.gif':
        FTYPE = 'GIF'
      elif thumb_extension == '.png':
        FTYPE = 'PNG'
      else:
        return False 
      
      data_img = BytesIO()
      image.save(data_img, FTYPE)
      data_img.seek(0)
      self.thumbnail.save(thumb_filename, ContentFile(data_img.read()), save=False)
      data_img.close()
        
    super(UserAccount , self).save(*args , **kwargs)

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'
    ordering = ['id']  

  def get_full_name(self):
    return f"#{self.first_name}  {self.last_name}"

  def get_short_name(self):
    return f"{self.first_name}"

  def __str__(self):
    return f"{self.email}"

  def update_field(self, field, value):
    current_instance = self
    setattr(current_instance, field, value)
    current_instance.save()
    return current_instance

  def allowed_fields_to_update(self):
    return [
      'email', 'first_name', 'last_name',
    ]
