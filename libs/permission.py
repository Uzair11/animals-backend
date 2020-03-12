from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class UserAccessPermission(permissions.BasePermission):
    message = 'Permission Denied'

    def has_permission(self, request, view):
        return request.user.is_active


class CustomerPermission(permissions.BasePermission):
    message = 'Permission Denied'

    def has_permission(self, request, view):
        return request.user.role == User.Role.CUSTOMER
