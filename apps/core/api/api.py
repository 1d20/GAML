from rest_framework.mixins import CreateModelMixin
from apps.core import models
from rest_framework import viewsets
from apps.core.api import ObjectSerializer


class SingerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Singer.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        singer_startswith = self.request.GET.get('letter', 'A')
        return self.queryset.filter(name__startswith=singer_startswith)


class SongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        singer_id = self.request.GET.get('singer', None)
        if not singer_id:
            return []
        return self.queryset.filter(singer_id=singer_id)


class SongInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SongInfo.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        song_id = self.request.GET.get('song', None)
        if not song_id:
            return []
        return self.queryset.filter(song_id=song_id)


class CommentViewSet(CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        song_id = self.request.GET.get('song', None)
        if not song_id:
            return []
        return self.queryset.filter(song_id=song_id)
#
