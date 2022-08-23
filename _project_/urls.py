from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from todo_list.api.routers import todo_list_router


api_routers = (todo_list_router.urls,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((todo_list_router.urls, 'api')))
]
