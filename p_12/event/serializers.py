from rest_framework import serializers
from .models import EventStatus, Event

class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ("status",)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("client_id", 
                "date_created", 
                "date_updated", 
                "user_id", 
                "event_status_id", 
                "attendees", 
                "event_date", 
                "note")