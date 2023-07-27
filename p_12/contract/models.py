from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    mobile = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Contract(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Contract: ' + self.client_id.first_name
