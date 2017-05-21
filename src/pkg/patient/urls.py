from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from src.pkg.patient.views import PatientViewSet
from src.pkg.patient.views import CurrentPatientsView
from src.pkg.patient.views import DoctorConnectFinishView


router = DefaultRouter()
router.register(r'v1/patients', PatientViewSet, 'patient')

urlpatterns = router.urls + [
    url(r'^v1/current-patients/$', CurrentPatientsView.as_view(),
        name='apicurrent-patients'),
]
