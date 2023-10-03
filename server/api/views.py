from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet

from .models import Title, Chapter
from .serializers.chapter import ChapterDetailSerializer
from .serializers.title import TitleListSerializer, TitleDetailSerializer
from .tasks import register_view_task, register_like_task


class TitleAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'count'
    max_page_size = 5


class ChapterAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    max_page_size = 50


class ChapterViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterDetailSerializer
    pagination_class = ChapterAPIListPagination

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        register_view_task.delay(obj.id)
        return super().retrieve(request, *args, **kwargs)

    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        obj = self.get_object()
        register_like_task.delay(obj.id)
        return Response({
            'response': 'Лайк поставлен',
        })


class TitleViewsSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleListSerializer
    pagination_class = TitleAPIListPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TitleDetailSerializer
        return TitleListSerializer
