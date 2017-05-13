from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from src.pkg.patient.views import PatientViewSet
from src.pkg.patient.views import CurrentPatientsView


router = DefaultRouter()
router.register(r'v1/patients', PatientViewSet, 'patient')

urlpatterns = router.urls + [
    url(r'^api/v1/current$', CurrentPatientsView.as_view(),
        name='apicurrent-patients')
]
