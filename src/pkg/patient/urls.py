from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from pkg.patient.views import PatientViewSet

router = DefaultRouter()
router.register(r'v1/patients', PatientViewSet, 'patient')

urlpatterns = router.urls
