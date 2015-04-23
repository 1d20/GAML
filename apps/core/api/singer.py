from apps.core import models
from rest_framework import serializers, viewsets


class SingerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Singer
        fields = ('name', 'description')


class SingerViewSet(viewsets.ModelViewSet):
    queryset = models.Singer.objects.all()
    serializer_class = SingerSerializer


