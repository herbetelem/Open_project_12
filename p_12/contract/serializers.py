from rest_framework import serializers
from .models import Client, Contract

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("first_name", 
                "last_name", 
                "email", 
                "phone", 
                "mobile", 
                "company_name", 
                "date_created", 
                "date_updated", 
                "sales_contact")

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("user_id", 
                "client_id", 
                "status", 
                "amount", 
                "payment_due",  
                "date_created", 
                "date_updated")
