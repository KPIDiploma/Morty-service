import base64
from datetime import datetime
import logging

import rsa
from rest_framework import permissions

from django.conf import settings

logger = logging.getLogger('file')

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
            logger.error(e)
            token_timestamp = token
        except:
            logger.error(e)
            return False

        try:
            time = datetime.strptime(
                token_timestamp,
                '%Y-%m-%d %H:%M:%S'
            )
        except:
            logger.error(e)
            return False

        now_time = datetime.utcnow()
        delta = now_time - time
        logger.info(delta)
        if delta.seconds > 300:
            logger.error(e)
            return False
        if doctor_id:
            request.session['doctor_id'] = doctor_id
        return True
