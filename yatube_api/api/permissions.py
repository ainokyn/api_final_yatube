from rest_framework import permissions, status


class AuthorPermission(permissions.BasePermission):
    message = status.HTTP_403_FORBIDDEN

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
