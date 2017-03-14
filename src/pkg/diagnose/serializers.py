from rest_framework import serializers
from pkg.diagnose.models import Diagnose
from pkg.diagnose.models import DiagnoseFile


class DiagnoseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnoseFile
        fields = ('id', 'file')


class DiagnoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnose
        fields = ('id', 'text', 'attached_files')
