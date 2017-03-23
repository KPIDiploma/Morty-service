from rest_framework import viewsets

from pkg.diagnose.models import Diagnose
from pkg.diagnose.models import DiagnoseFile
from pkg.diagnose.serializers import DiagnoseSerializer
from pkg.diagnose.serializers import FileSerializer
from pkg.common.permissions import IsCurrentUserOrAdminOnly


class DiagnoseViewSet(viewsets.ModelViewSet):
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseSerializer
    permission_classes = (IsCurrentUserOrAdminOnly,)


class DiagnoseFileViewSet(viewsets.ModelViewSet):
    queryset = DiagnoseFile.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsCurrentUserOrAdminOnly,)
