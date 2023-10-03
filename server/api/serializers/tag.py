from rest_framework.serializers import ModelSerializer

from ..models import Tag


class TagDetailSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
