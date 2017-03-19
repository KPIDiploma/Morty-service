from .models import Diagnose
from .models import DiagnoseFile
from django.contrib import admin


class DiagnoseFilesInline(admin.ModelAdmin):
    pass


class DiagnoseAdmin(admin.ModelAdmin):
    pass


admin.site.register(DiagnoseFile, DiagnoseFilesInline)
admin.site.register(Diagnose, DiagnoseAdmin)
