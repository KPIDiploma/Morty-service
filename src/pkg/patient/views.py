from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

from pkg.patient.models import Patient
from pkg.patient.serializers import PatientSerializer
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
        # return render(request, 'patient/profile.html')
        return redirect('profile', request)
    else:
        return redirect('/', request)


@login_required(login_url='/login')
def profile(request):
    return render(request, 'patient/profile.html')


# @login_required(redirect_field_name=)
# @permission_classes((IsCurrentUserOrAdminOnly,))
# def current(request):
#     """
#     Returns actual order of the current user
#     """
#     serializer = PatientSerializer(request.user)
#     return Response(serializer.data)


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
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
