from rest_framework.serializers import ModelSerializer
from ..models import Chapter


class ChapterDetailSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
