from .models import Diagnose
from .models import DiagnoseFiles
from django.contrib import admin


class DiagnoseFilesInline(admin.ModelAdmin):
    pass


class DiagnoseAdmin(admin.ModelAdmin):
    pass

admin.site.register(DiagnoseFiles, DiagnoseFilesInline)
admin.site.register(Diagnose, DiagnoseAdmin)
