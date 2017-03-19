from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from pkg.diagnose.models import Diagnose
from pkg.diagnose.models import DiagnoseFile
from pkg.diagnose.serializers import DiagnoseSerializer
from pkg.diagnose.serializers import DiagnoseFileSerializer
from pkg.common.permissions import IsCurrentUserOrAdminOnly


@api_view(['GET', ])
@permission_classes((IsCurrentUserOrAdminOnly,))
def current(request):
    """
    Returns actual order of the current user
    """
    serializer = DiagnoseSerializer(request.user)
    return Response(serializer.data)


class DiagnoseViewSet(viewsets.ModelViewSet):
    queryset = Diagnose.objects.all()
    serializer_class = DiagnoseSerializer
    permission_classes = (IsCurrentUserOrAdminOnly,)


class DiagnoseFileViewSet(viewsets.ModelViewSet):
    queryset = DiagnoseFile.objects.all()
    serializer_class = DiagnoseFileSerializer
    permission_classes = (IsCurrentUserOrAdminOnly,)
