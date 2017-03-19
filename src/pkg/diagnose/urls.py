from rest_framework.routers import DefaultRouter

from pkg.diagnose.views import DiagnoseFileViewSet
from pkg.diagnose.views import DiagnoseViewSet

router = DefaultRouter()
router.register(r'v1/diagnose', DiagnoseViewSet, 'diagnose')
router.register(r'v1/files', DiagnoseFileViewSet, 'files')

urlpatterns = router.urls
