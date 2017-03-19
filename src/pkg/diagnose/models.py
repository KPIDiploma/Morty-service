from django.db import models


# Create your models here.
class Diagnose(models.Model):
    text = models.TextField()

    def __str__(self):
        return str(self.pk)


class DiagnoseFile(models.Model):
    file = models.FileField()
    diagnose = models.ForeignKey(Diagnose, related_name='files',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.file)
