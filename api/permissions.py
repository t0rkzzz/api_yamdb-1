from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS

User = get_user_model()


class IsAdmin(BasePermission):
    allowed_user_roles = ('admin',)

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role in self.allowed_user_roles:
                return True
        return False


class IsAuthorOrIsAdminOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            if request.user.role in ('admin',):
                return True
        return obj.author == request.user


class IsGetOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            if request.user.role in ('admin',):
                return True
        return False
