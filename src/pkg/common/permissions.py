from rest_framework import permissions


class IsCurrentUserOrAdminOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)

        if request.method == 'POST':
            return is_admin

        return True

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.pk == obj.pk


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff or obj.owner == request.user


class MyTokenPermission(permissions.AllowAny):
    def has_permission(self, request, view):
        token = request.query_params.get('token')
        if token:
            return True
        return False
