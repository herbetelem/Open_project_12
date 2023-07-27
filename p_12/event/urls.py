

from importlib.resources import path

# from rest_framework_nested import routers
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("eventstatus", views.EventStatusViewSet, basename="eventstatus")
router.register("event", views.EventViewSet, basename="event")

urlpatterns = [
    path("", include(router.urls)),
]
