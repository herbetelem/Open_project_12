# import python

# import django
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# import tier
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

# import perso
from .models import Event, EventStatus
from .serializers import EventSerializer, EventStatusSerializer

from django.shortcuts import render, get_object_or_404, redirect
from .permission import CheckRolePermission


# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated, CheckRolePermission]

class EventStatusViewSet(viewsets.ModelViewSet):
    queryset = EventStatus.objects.all()
    serializer_class = EventStatusSerializer

    permission_classes = [IsAuthenticated, CheckRolePermission]
