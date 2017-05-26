from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response

from src.pkg.common.pagination import StandardResultsSetPagination
from src.pkg.common.permissions import MyTokenPermission
from src.pkg.diagnose.models import Diagnose
from src.pkg.diagnose.models import DiagnoseFile
from src.pkg.diagnose.serializers import *
from src.pkg.patient.models import Patient


__all__ = [
    'PatientSerializer', 'FullPatientSerializer',
    'PatientRegisterSerializer', 'PatientUpdatePasswordSerializer'
]


class DiagnoseViewSet(viewsets.ModelViewSet):
    """
    POST
    {
     "text":"Diagnose1",
     "patient": <patient_id>,
     "doctor": "Ai bolit"
    }
    """
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseForPatientSerializer
    permission_classes = (MyTokenPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('text',)
    pagination_class = StandardResultsSetPagination

    def retrieve(self, request, pk=None, *args, **kwargs):
        diagnose = get_object_or_404(self.queryset, pk=pk)
        serializers = DiagnoseWithFileSerializer(diagnose)
        return Response(serializers.data)

    def create(self, request, *args, **kwargs):
        serializer = DiagnosePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DiagnoseFileViewSet(viewsets.ModelViewSet):
#     queryset = Diagnose.objects.all()
#     serializer_class = DiagnoseWithFileSerializer
#     permission_classes = (IsCurrentUserOrAdminOnly,)


class FileViewSet(viewsets.ModelViewSet):
    queryset = DiagnoseFile.objects.all()
    serializer_class = FileSerializer
    permission_classes = (MyTokenPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('file',)
    pagination_class = StandardResultsSetPagination


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


@login_required(login_url='/login')
def diagnoses(request):
    return render(request, 'diagnoses/index.html')
