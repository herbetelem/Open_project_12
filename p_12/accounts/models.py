from tabnanny import verbose
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class UserTheme(models.Model):
    THEME_CHOICES = (
        ('cyborg', 'cyborg'),
        ('cerulean', 'cerulean'),
        ('lux', 'lux'),
        ('lumen', 'lumen'),
        ('simplex', 'simplex'),
        ('morph', 'morph'),
        ('minty', 'minty'),
        ('slate', 'slate'),
        ('vapor', 'vapor'),
        ('zephyr', 'zephyr'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(choices=THEME_CHOICES, default='cyborg', max_length=10)

    def __str__(self):
        return "theme: " + self.user.username


class UserRole(models.Model):
    ROLE_CHOICE = (
        ('default', 'default'),
        ('support_team', 'support_team'),
        ('management_team', 'management_team'),
        ('sales_team', 'sales_team'),
    )    
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    role = models.CharField(choices=ROLE_CHOICE, default='default', max_length=15)


    def __str__(self):
        return self.user.username + ' -> ' + self.role
