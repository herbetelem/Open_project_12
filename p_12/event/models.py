from django.db import models
from django.contrib.auth.models import User
from contract.models import Client

# Create your models here.
class EventStatus(models.Model):
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.status


class Event(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_status_id = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return 'Event: ' + self.client_id.first_name
