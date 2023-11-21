"""
URL configuration for GRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from core.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title='GRIEVANCE REDRESS MECHANISM API',
        default_version='v1',
        description='Yet Another GRM API',
        contact=openapi.Contact(email='issajuma11@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include([
        path('', include('core.urls'), name='api-list'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('admin/', admin.site.urls),
        # path('core/api/auth', include('rest_framework.urls')),
        path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('auth/', include('djoser.urls')),
        # path('obtain/', DecoratedTokenObtainPairView.as_view(), name='obtain-token'),
        # path('refresh/', DecoratedTokenRefreshView.as_view(), name='refresh-token'),
        # path('obtain/', DecoratedTokenVerifyView.as_view(), name='verify-token'),
        # path('obtain/', DecoratedTokenBlacklistView.as_view(), name='blacklist-token'),
        path('auth/', include('djoser.urls.jwt'))
    ])),
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
