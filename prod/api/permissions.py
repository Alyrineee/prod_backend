from api.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsRoomAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.data.keys().__contains__("user"):
            user_password = get_object_or_404(
                User.objects.all(), pk=request.data["user"][0]
            ).password
            if request.data["user_password"] == user_password:
                return True
            else:
                return False
