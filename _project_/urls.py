from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from todo_list.api.routers import todo_list_router


api_routers = (todo_list_router.urls,)

schema_view = get_schema_view(  # noqa: pylint=invalid-name
   openapi.Info(
      title="API",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((todo_list_router.urls, 'api'))),
    path('auth/', include(('custom_auth.urls', 'auth'))),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
