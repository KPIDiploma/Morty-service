from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated

from pkg.patient.models import Patient
from pkg.patient.serializers import PatientSerializer
from pkg.patient.serializers import PatientRegisterSerializer
from pkg.common.permissions import IsCurrentUserOrAdminOnly


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsCurrentUserOrAdminOnly,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class RegistrationView(generics.CreateAPIView):
    """
    Use this endpoint to register new user.
    After the registration to the specified email
    will receive a message of activation.
    """
    serializer_class = PatientRegisterSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )