from rest_framework.routers import SimpleRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import register_view, login_view
from .views import UsersViewSet

router = SimpleRouter()
router.register('users', UsersViewSet)

urlpatterns = [
  path('login/', login_view, name='login'),
  path('register/', register_view, name='register')
]

urlpatterns += staticfiles_urlpatterns()