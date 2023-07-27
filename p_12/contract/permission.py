from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class CheckRolePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if view.basename == 'client' or view.basename == 'contract':
            users = User.objects.filter(id=request.user.id)
            if users.exists():
                user = users.first()
                groups = user.groups.all()
                for group in groups:
                    group_name = group.name
                    if group_name == 'admin' or group_name == 'sales_team':
                        return True
                return False
            return False
        return False
