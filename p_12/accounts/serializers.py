from rest_framework import serializers
from .models import UserRole, UserTheme

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ("role", "user", "id")


class UserThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTheme
        fields = ("theme", "user", "id")
