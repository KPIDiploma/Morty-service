from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login

from pkg.patient.models import Patient
from pkg.patient.serializers import PatientSerializer
from pkg.patient.serializers import FullPatientSerializer
from pkg.patient.serializers import PatientRegisterSerializer
from pkg.common.permissions import IsCurrentUserOrAdminOnly


def index(request):
    return render(request, 'patient/index.html')


def login_view(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/profile', request)
    else:
        return redirect('/', request)


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

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = Patient.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = FullPatientSerializer(patient)
        return Response(serializer.data)

    def partial_update(self, request, pk=None, *args, **kwargs):
        queryset = Patient.objects.all()
        patient = get_object_or_404(queryset, pk=pk)
        serializer = FullPatientSerializer(patient)
        return Response(serializer.data)

    def perform_update(self, serializer):
        # queryset = Patient.objects.all()
        # patient = get_object_or_404(queryset, pk=pk)
        # if request.data
        # patient.save()
        # serializer = FullPatientSerializer(patient)
        serializer.save()
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
