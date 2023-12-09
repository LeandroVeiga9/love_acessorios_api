from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import UserAccount

User = get_user_model()

class UserSerializer(UserCreateSerializer):
    
  class Meta(UserCreateSerializer.Meta):
    model = User
    fields = (
      'id',
      'thumbnail', 'email', 'first_name', 'last_name', 'password', 'profile_image', 'profile_image_url',
      'is_active', 'created_at', 'updated_at', 'is_staff', 'phone_number'
    )

class UserLoginSerializer(UserSerializer):
  token = serializers.SerializerMethodField(method_name='getToken')

  class Meta(UserCreateSerializer.Meta):
    model = User
    fields = (
      'id',
      'thumbnail', 'email', 'first_name', 'last_name', 'password', 'profile_image', 'profile_image_url',
      'is_active', 'created_at', 'updated_at', 'is_staff', 'phone_number', 'token'
    )

  def getToken(self, ownerObj):
    refresh = RefreshToken.for_user(ownerObj)
    return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
    }