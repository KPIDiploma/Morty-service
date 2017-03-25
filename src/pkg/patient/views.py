import json

from rest_framework import viewsets
from rest_framework import status
from rest_framework import views
from rest_framework import serializers
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from pkg.patient.models import Patient
from pkg.patient.serializers import PatientSerializer
from pkg.patient.serializers import FullPatientSerializer
from pkg.patient.serializers import PatientRegisterSerializer


def index(request):
    if request.user.is_authenticated:
        return redirect('/api/v1/profile', request)
    return render(request, 'patient/index.html')


class LogoutView(generics.GenericAPIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = serializers.Serializer

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(views.APIView):
    def post(self, request, format=None):

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = PatientSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


@login_required(login_url='/login')
def profile(request):
    return render(request, 'patient/profile.html')


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Patient.objects.all()
    serializer_class = FullPatientSerializer

    def list(self, request, *args, **kwargs):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)


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
