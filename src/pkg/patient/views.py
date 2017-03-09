from pkg.patient.models import Patient
from pkg.patient.serializers import PatientSerializer
from rest_framework import viewsets


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

