from apps.core import models
from rest_framework import serializers, viewsets


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Song
        fields = ('singer', 'title')


class SongViewSet(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = SongSerializer


