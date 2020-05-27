"""LPGallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions, routers

from gallery.views import CommunityViewSet, LPModelViewSet, CommentViewSet, MainPageViewSet

from security.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'communities', CommunityViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'main-pages', MainPageViewSet)
router.register(r'lpmodels', LPModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('security.urls', 'security'), namespace='security')),
    path('', include(('gallery.urls', 'gallery'), namespace='gallery')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

schema_view = get_schema_view(
    openapi.Info(
        title="LPGallery API",
        default_version='v1',
        description="LPGallery description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alexermakovx@gmail.com"),
        license=openapi.License(name='Some License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_schema_view = get_swagger_view(title='LPGallery API')

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
urlpatterns += [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

handler500 = 'security.views.internal_server_error'
handler404 = 'security.views.page_not_found'
