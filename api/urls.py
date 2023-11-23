from rest_framework.routers import SimpleRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


router = SimpleRouter()

from .views import register_view, login_view


urlpatterns = [
  path('login/', login_view, name='login'),
  path('register/', register_view, name='register')
]

urlpatterns += staticfiles_urlpatterns()