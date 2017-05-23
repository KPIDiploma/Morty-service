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
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from src.pkg.patient.models import Patient, Doctor
from src.pkg.patient.serializers import *
from src.pkg.patient.services import PatientService

from src.pkg.common.filters import IsAuthorFilterBackend
from src.pkg.common.permissions import MyTokenPermission
from src.pkg.common.pagination import StandardResultsSetPagination


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
        serializer = PatientCurrentUserSerializer(patient)
        return Response(serializer.data)


class CurrentUserFilesView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        patient = Patient.objects.get(pk=request.user.id)
        serializer = PatientCurrentUserSerializer(patient)
        return Response(serializer.data)


class RegistrationView(generics.CreateAPIView):
    """
    Use this endpoint to register new user.
    After the registration to the specified email
    will receive a message of activation.
    POST 
    {
        email:'',
        birthday: mm/dd/yyyy
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
    serializer_class = FullPatientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fullname',)
    pagination_class = StandardResultsSetPagination

    # filter_backends = (IsAuthorFilterBackend,)

    def retrieve(self, request, pk=None, *args, **kwargs):
        doctor_id = request.session.get('doctor_id', None)
        if doctor_id:
            try:
                patient = get_object_or_404(
                    self.queryset,
                    pk=pk,
                    doctors__id=doctor_id)
                serializers = FullPatientSerializer(patient)
                return Response(serializers.data)

            except Exception as e:
                return Response({
                    'error': True,
                    'message': 'msg={}\n DocId={}'.format(str(e), doctor_id)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'error': True,
                'message': 'Doctor id not found'
            }, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        doctor_id = request.data.get('id', None)
        doctor_fullname = request.data.get('fullname', None)
        if doctor_id and doctor_fullname:
            patient = get_object_or_404(self.queryset, pk=pk)
            doctor, created = Doctor.objects.get_or_create(pk=doctor_id)
            if created:
                doctor.fullname = doctor_fullname
                doctor.save()

            try:
                PatientService.connect_patient(patient.id, int(doctor_id))
                # PatientService.try_connect_doctor(doctor, patient)
            except Exception as e:
                return Response({
                    'error': True,
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'error': False,
                'message': 'Send connection request'
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                'error': True,
                'message': 'doctor id or fullname not found'
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response({
            'error': True,
            'message': 'Not implemented'
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({
            'error': True,
            'message': 'Not implemented'
        }, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        return Response({
            'error': True,
            'message': 'Not implemented'
        }, status=status.HTTP_400_BAD_REQUEST)


class DoctorConnectFinishView(generics.GenericAPIView):
    """
    Use this endpoint to finish doctor connection.
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        doctor_token = request.query_params.get('doctor')[2:-1]
        connected = PatientService().final_connect_doctor(request.user,
                                                          doctor_token,
                                                          token)
        if connected:
            return render(request, 'patient/doctor_connected.html')
        else:
            return render(request, 'patient/error.html')


class CurrentPatientsView(generics.ListAPIView):
    permission_classes = (MyTokenPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fullname',)
    pagination_class = StandardResultsSetPagination
    serializer_class = FullPatientSerializer

    def get_queryset(self):
        print(self.request.session.get('doctor_id', None))
        return Patient.objects.filter(
            doctors__id=self.request.session.get('doctor_id', None)
        )
