from rest_framework.serializers import ModelSerializer

from ..models import Title
from .tag import TagDetailSerializer
from .volume import VolumeDetailSerializer


class TitleDetailSerializer(ModelSerializer):
    tags = TagDetailSerializer(many=True)
    volumes = VolumeDetailSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'


class TitleListSerializer(ModelSerializer):
    tags = TagDetailSerializer(many=True)

    class Meta:
        model = Title
        fields = '__all__'
