from rest_framework import serializers
from src.pkg.diagnose.models import Diagnose
from src.pkg.diagnose.models import DiagnoseFile

from src.pkg.patient.models import Patient


__all__ = [
    "FileSerializer",
    "DiagnoseFileSerializer",
    "DiagnoseWithFileSerializer",
    "DiagnosePostSerializer",
    "DiagnoseForPatientSerializer",
    "PatientCurrentUserSerializer",
]


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
        fields = ('id', 'text', 'patient', 'doctor', 'date', 'files')


class DiagnosePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnose
        fields = ('id', 'text', 'patient', 'doctor')


class DiagnoseForPatientSerializer(serializers.ModelSerializer):
    files = DiagnoseFileSerializer(many=True, required=False)

    class Meta:
        model = Diagnose
        fields = ('id', 'text', 'doctor', 'date', 'files')


class PatientCurrentUserSerializer(serializers.ModelSerializer):
    diagnoses = DiagnoseForPatientSerializer(many=True)

    class Meta:
        model = Patient
        fields = ('diagnoses',)
