from django.db import models

from src.pkg.patient.models import Patient
from src.pkg.patient.models import Doctor


# Create your models here.
class Diagnose(models.Model):
    text = models.TextField()
    diagnose = models.ForeignKey(Patient, related_name='diagnoses',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class DiagnoseFile(models.Model):
    file = models.FileField()
    diagnose = models.ForeignKey(Diagnose, related_name='files',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.file)
