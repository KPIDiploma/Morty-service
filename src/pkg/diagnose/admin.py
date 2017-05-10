from src.pkg.diagnose.models import Diagnose
from src.pkg.diagnose.models import DiagnoseFile
from django.contrib import admin


class DiagnoseFilesInline(admin.ModelAdmin):
    pass


class DiagnoseAdmin(admin.ModelAdmin):
    pass


admin.site.register(DiagnoseFile, DiagnoseFilesInline)
admin.site.register(Diagnose, DiagnoseAdmin)
