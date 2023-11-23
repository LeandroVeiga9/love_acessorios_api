from rest_framework import viewsets

from ..models import UserAccount

from ..serializers import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer

