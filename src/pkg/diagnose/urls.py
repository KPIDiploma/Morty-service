from rest_framework.routers import DefaultRouter

# from src.pkg.diagnose.views import DiagnoseFileViewSet
from src.pkg.diagnose.views import FileViewSet
from src.pkg.diagnose.views import DiagnoseViewSet


router = DefaultRouter()
router.register(r'v1/diagnose', DiagnoseViewSet, 'diagnose')
# router.register(r'v1/diagnose', DiagnoseViewSet, 'diagnose')
router.register(r'v1/files', FileViewSet, 'files')

urlpatterns = router.urls
