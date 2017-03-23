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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pkg.patient.views import RegistrationView
from pkg.patient.views import profile
from pkg.patient.views import index
from pkg.patient.views import LoginView
from pkg.patient.views import logout_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'profile', profile, name='profile'),

    url(r'^admin/', admin.site.urls),
    url(r'api/', include('pkg.patient.urls', namespace='api')),
    url(r'api/', include('pkg.diagnose.urls', namespace='api')),
    url(r'^api/v1/register/', RegistrationView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # urlpatterns += staticfiles_urlpatterns()
