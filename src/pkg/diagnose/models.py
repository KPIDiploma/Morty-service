from django.db import models


class DiagnoseFiles(models.Model):
    file = models.FileField()


# Create your models here.
class Diagnose(models.Model):
    text = models.TextField()
    attached_files = models.ManyToManyField(DiagnoseFiles)
