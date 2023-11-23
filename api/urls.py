from rest_framework.routers import SimpleRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


router = SimpleRouter()

urlpatterns = [
]

urlpatterns += staticfiles_urlpatterns()