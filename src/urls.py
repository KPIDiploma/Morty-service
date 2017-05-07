"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from src.pkg.patient.views import RegistrationView
from src.pkg.patient.views import profile
from src.pkg.patient.views import index
from src.pkg.patient.views import LoginView
from src.pkg.patient.views import LogoutView
from src.pkg.patient.views import CurrentUserView
from src.pkg.patient.views import CurrentUserDiagnosesView
from src.pkg.patient.views import CurrentUserFilesView


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/v1/auth/login$', LoginView.as_view(), name='apilogin'),
    url(r'^api/v1/auth/logout$', LogoutView.as_view(),
        name='apilogout'),
    url(r'^api/v1/current-user$', CurrentUserView.as_view(),
        name='apicurrent-user'),
    url(r'^api/v1/current-diagnoses$', CurrentUserDiagnosesView.as_view(),
        name='apicurrent-diagnose'),
    url(r'^api/v1/current-files/(?P<pk>[0-9]+)$',
        CurrentUserFilesView.as_view(), name='apicurrent-files'),
    url(r'^profile$', profile, name='profile'),

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('src.pkg.patient.urls', namespace='api')),
    url(r'^api/', include('src.pkg.diagnose.urls', namespace='api')),
    url(r'^api/v1/register/', RegistrationView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
