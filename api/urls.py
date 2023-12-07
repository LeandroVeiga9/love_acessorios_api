from rest_framework.routers import SimpleRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import register_view, login_view
from .views import UsersViewSet, ProductsViewSet, CategoriesViewSet, VariantsViewSet, CartsViewSet

router = SimpleRouter()
router.register('users', UsersViewSet)
router.register('products', ProductsViewSet)
router.register('categories', CategoriesViewSet)
router.register('variants', VariantsViewSet)
router.register('carts', CartsViewSet)

urlpatterns = [
  path('login/', login_view, name='login'),
  path('register/', register_view, name='register')
]

urlpatterns += staticfiles_urlpatterns()