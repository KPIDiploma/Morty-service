from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from src.pkg.diagnose.models import Diagnose
from src.pkg.diagnose.models import DiagnoseFile
from src.pkg.diagnose.serializers import DiagnoseSerializer
from src.pkg.diagnose.serializers import DiagnoseWithFileSerializer
from src.pkg.diagnose.serializers import FileSerializer
from src.pkg.common.permissions import MyTokenPermission


class DiagnoseViewSet(viewsets.ModelViewSet):
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseSerializer
    permission_classes = (MyTokenPermission,)

    def retrieve(self, request, pk=None, *args, **kwargs):
        diagnose = get_object_or_404(self.queryset, pk=pk)
        serializers = DiagnoseWithFileSerializer(diagnose)
        return Response(serializers.data)


# class DiagnoseFileViewSet(viewsets.ModelViewSet):
#     queryset = Diagnose.objects.all()
#     serializer_class = DiagnoseWithFileSerializer
#     permission_classes = (IsCurrentUserOrAdminOnly,)


class FileViewSet(viewsets.ModelViewSet):
    queryset = DiagnoseFile.objects.all()
    serializer_class = FileSerializer
    permission_classes = (MyTokenPermission,)
