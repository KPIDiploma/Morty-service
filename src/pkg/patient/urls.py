from rest_framework.routers import DefaultRouter

from pkg.patient.views import PatientViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, 'patient')

urlpatterns = router.urls
