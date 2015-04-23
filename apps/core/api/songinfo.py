from apps.core import models
from rest_framework import serializers, viewsets


class SongInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SongInfo
        fields = ('song', 'site', 'media_url', 'media_info', 'song_text')


class SongInfoViewSet(viewsets.ModelViewSet):
    queryset = models.SongInfo.objects.all()
    serializer_class = SongInfoSerializer


