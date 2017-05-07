from rest_framework import serializers
from src.pkg.diagnose.models import Diagnose
from src.pkg.diagnose.models import DiagnoseFile


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnoseFile
        fields = ('id', 'file', 'diagnose')


class DiagnoseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnoseFile
        fields = ('id', 'file',)


class DiagnoseWithFileSerializer(serializers.ModelSerializer):
    files = DiagnoseFileSerializer(many=True, required=False)

    class Meta:
        model = Diagnose
        fields = ('id', 'text', 'patient', 'files')


class DiagnoseSerializer(serializers.ModelSerializer):
    # patient = PatientSerializer()

    class Meta:
        model = Diagnose
        fields = ('id', 'text')
