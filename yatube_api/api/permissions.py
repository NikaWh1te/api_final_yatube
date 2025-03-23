from rest_framework import permissions


class IsAuthenticatedOrOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return True  # Разрешаем доступ на уровень вьюсета, объектные права проверяются отдельно

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
