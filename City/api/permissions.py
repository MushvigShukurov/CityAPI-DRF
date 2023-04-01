from rest_framework import permissions

class IsAuthOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or bool(request.user and request.user.is_authenticated)