from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate
from drf_yasg import openapi

from ..serializers import UserSerializer, UserLoginSerializer

from ..models import UserAccount

import re

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
  required_fields = ['email', 'password']
  if not all(value in request.data for value in required_fields):
    return Response({'message': 'Wrong email and/or password'}, status=404)
  
  user = authenticate(email=request.data['email'], password=request.data['password'])
  
  if user is not None:
    serializer_user = UserLoginSerializer(user, context={'request': request}).data
    return Response({**serializer_user}, status=200)
  else:
    message = 'Email/Password invalid'
    return Response({'message': message}, status=404)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    data = request.data
    data['is_staff'] = False
    
    user_exists = UserAccount.objects.filter(email=data['email']).exists()
    
    if user_exists:
      return Response([['This email is already in use.']], status=422)

    serializer = UserLoginSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()

        serializer_user = UserLoginSerializer(user, context={'request': request}).data
        return Response({**serializer_user}, status=201)
    else:
        return Response(serializer.errors, status=404)


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email(request):
    user_exists = UserAccount.objects.filter(email=request.data.get('email')).exists()
    return Response({'available_email': not user_exists}, status=200)

    