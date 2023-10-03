from django.contrib import admin
from django.urls import path, include
from api.routers import title_router, chapter_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(title_router.urls)),
    path('api/v1/', include(chapter_router.urls))
]
