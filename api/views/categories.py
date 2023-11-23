from ..models import Category
from ..serializers import CategoriesSerializer
from rest_framework import viewsets


class CategoriesViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategoriesSerializer
