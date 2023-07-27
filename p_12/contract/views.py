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
from .models import Client, Contract
from .serializers import ClientSerializer, ContractSerializer

from django.shortcuts import render, get_object_or_404, redirect
from .permission import CheckRolePermission


# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    permission_classes = [IsAuthenticated, CheckRolePermission]

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    permission_classes = [IsAuthenticated, CheckRolePermission]
