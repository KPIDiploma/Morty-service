from django.db import models
from django.utils.translation import ugettext as _

from src.pkg.patient.models import Patient
from src.pkg.patient.models import Doctor


# Create your models here.
class Diagnose(models.Model):
    text = models.TextField()
    patient = models.ForeignKey(Patient, related_name='diagnoses',
                                on_delete=models.CASCADE)
    doctor = models.CharField(
        verbose_name=_('doctor fullname'),
        max_length=300,
    )
    date = models.DateField(
        verbose_name=_('date of the birth'),
        auto_now=True
    )

    def __str__(self):
        return str(self.pk)


class DiagnoseFile(models.Model):
    file = models.FileField()
    diagnose = models.ForeignKey(Diagnose, related_name='files',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.file)
