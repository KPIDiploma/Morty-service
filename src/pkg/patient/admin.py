from .models import Patient
from django.contrib import admin


class PatientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)
