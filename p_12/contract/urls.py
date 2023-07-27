

from importlib.resources import path

# from rest_framework_nested import routers
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'client', views.ClientViewSet, basename='client')
router.register(r'contract', views.ContractViewSet, basename='contract')

urlpatterns = [
    path("", include(router.urls)),
]
