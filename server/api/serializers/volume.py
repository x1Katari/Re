from rest_framework.serializers import ModelSerializer

from ..models import Volume
from .chapter import ChapterDetailSerializer


class VolumeDetailSerializer(ModelSerializer):
    chapters = ChapterDetailSerializer(many=True)

    class Meta:
        model = Volume
        fields = '__all__'
