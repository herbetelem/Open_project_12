from django.contrib import admin
from .models import UserTheme, UserRole

# Register your models here.
admin.site.register(UserTheme)
admin.site.register(UserRole)