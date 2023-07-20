from rest_framework import serializers
from .models import Extra

class ExtraModelSerializer(serializers.ModelSerializer):
    """Extra Model Serializer"""

    class Meta:
        """Meta class."""

        model = Extra
        fields = (
            'pk',
            'expedition',
            'title',
            'url',
            'description',
        )

class ExtraSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    expedition = serializers.DateTimeField()
    title = serializers.CharField(max_length=250)
    url = serializers.URLField(required=False)
    description = serializers.CharField(max_length=5000)

    def create(self, data):

        extra = Extra.objects.create(**data)
        return extra