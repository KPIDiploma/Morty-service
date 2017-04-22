from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from pkg.patient.views import PatientViewSet
from pkg.patient.views import CurrentUserView


router = DefaultRouter()
router.register(r'v1/patients', PatientViewSet, 'patient')

urlpatterns = router.urls
