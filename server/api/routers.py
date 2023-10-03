from rest_framework import routers
from .views import TitleViewsSet, ChapterViewSet

title_router = routers.DefaultRouter()
title_router.register(
    prefix='title',
    viewset=TitleViewsSet
)

chapter_router = routers.DefaultRouter()
chapter_router.register(
    prefix='chapter',
    viewset=ChapterViewSet
)
