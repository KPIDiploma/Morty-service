from django.contrib import admin
from src.diagnose.models import Diagnose, DiagnoseFiles
from django.contrib import admin


class DiagnoseFilesInline(admin.StackedInline):
    fields = '__all__'

    def get_queryset(self, request):
        qs = super(DiagnoseFilesInline, self).get_queryset(request)
        return qs.filter(state__gt=10)


# Register your models here.
class DiagnoseAdmin(admin.ModelAdmin):
    inlines = [DiagnoseFilesInline]


# admin.site.register(DiagnoseFiles, DiagnoseFilesAdmin)
admin.site.register(Diagnose, DiagnoseAdmin)
