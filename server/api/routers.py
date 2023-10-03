from rest_framework import routers
from .views import TitleViewsSet

title_router = routers.DefaultRouter()
title_router.register(
    prefix='title',
    viewset=TitleViewsSet
)
