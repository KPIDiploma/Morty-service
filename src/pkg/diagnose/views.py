from pkg.diagnose.models import Diagnose
from pkg.diagnose.models import DiagnoseFile
from pkg.diagnose.serializers import DiagnoseSerializer
from pkg.diagnose.serializers import DiagnoseFileSerializer
from rest_framework import viewsets


class DiagnoseViewSet(viewsets.ModelViewSet):
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseSerializer


class DiagnoseFileViewSet(viewsets.ModelViewSet):
    queryset = DiagnoseFile.objects.all()
    serializer_class = DiagnoseFileSerializer
