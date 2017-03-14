from django.db import models


class DiagnoseFile(models.Model):
    file = models.FileField()

    def __str__(self):
        return str(self.file)


# Create your models here.
class Diagnose(models.Model):
    text = models.TextField()
    attached_files = models.ManyToManyField(DiagnoseFile)

