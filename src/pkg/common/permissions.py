import base64
from datetime import datetime

import rsa
from rest_framework import permissions

from django.conf import settings


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
        # return True
        doctor_id = None
        token = request.query_params.get('token')
        if not token:
            return False
        try:
            token = base64.urlsafe_b64decode(token)
            token = rsa.decrypt(
                token,
                rsa.PrivateKey(**settings.SANYA_CLINIC_PRIVATE_KEY)
            ).decode()
            token_timestamp, doctor_id = token.split('/')
        except ValueError as e:
            token_timestamp = token
        except:
            return False

        try:
            time = datetime.strptime(
                token_timestamp,
                '%Y-%m-%d %H:%M:%S'
            )
        except:
            return False

        now_time = datetime.utcnow()
        delta = now_time - time
        if delta.seconds > 300:
            return False
        if doctor_id:
            request.session['doctor_id'] = doctor_id
        return True
