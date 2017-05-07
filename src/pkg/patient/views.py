import json

from rest_framework import viewsets
from rest_framework import status
from rest_framework import views
from rest_framework import serializers
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from src.pkg.patient.models import Patient
from src.pkg.common.filters import IsAuthorFilterBackend
from src.pkg.common.permissions import MyTokenPermission
from src.pkg.patient.pagination import StandardResultsSetPagination
from src.pkg.patient.serializers import *


def index(request):
    if request.user.is_authenticated:
        return redirect('/profile', request)
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

                return Response(status=status.HTTP_200_OK)
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


class CurrentUserView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        patient = Patient.objects.get(pk=request.user.id)
        serializer = FullPatientSerializer(patient)
        return Response(serializer.data)


class CurrentUserDiagnosesView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        patient = Patient.objects.get(pk=request.user.id)
        serializer = PatientDiagnosesSerializer(patient)
        return Response(serializer.data)


class CurrentUserFilesView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        patient = Patient.objects.get(pk=request.user.id)
        serializer = PatientDiagnosesSerializer(patient)
        return Response(serializer.data)


class RegistrationView(generics.CreateAPIView):
    """
    Use this endpoint to register new user.
    After the registration to the specified email
    will receive a message of activation.
    POST 
    {
        email:'',
        password:'',
        password_confirm:'',
        fullname:''
    }
    """
    serializer_class = PatientRegisterSerializer
    permission_classes = (MyTokenPermission,)


class UpdatePasswordView(generics.GenericAPIView):
    """
    Use this endpoint to update password for current user.
    """
    serializer_class = PatientUpdatePasswordSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request, *args, **kwargs):
        data = request.data
        data.update({'email': request.user.email})
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        return Response(sz.data, status=status.HTTP_200_OK)


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = (MyTokenPermission,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fullname',)
    pagination_class = StandardResultsSetPagination

    # filter_backends = (IsAuthorFilterBackend,)

    def get(self, request, *args, **kwargs):
        queryset = Patient.get_current_patients(request.user)
        serializer = PatientSerializer(queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['post', ])
    def add_patient(self, request, *args, **kwargs):
        token = request.query_params.get('token')

        doctor = Patient.objects.get(email=request.user.email)
        data = request.data
        doctor.patients.add()
        return Response(
            # data=BookSerializer(book).data,
            status=status.HTTP_200_OK)
