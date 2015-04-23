from apps.core import models
from rest_framework import viewsets
from apps.core.api import ObjectSerializer


class SingerViewSet(viewsets.ModelViewSet):
    queryset = models.Singer.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return self.queryset.filter(name__startswith=self.request.GET.get('letter', 'A'))


class SongViewSet(viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return self.queryset.filter(singer_id=self.request.GET.get('singer', None))


class SongInfoViewSet(viewsets.ModelViewSet):
    queryset = models.SongInfo.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return self.queryset.filter(song_id=self.request.GET.get('song', None))


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = ObjectSerializer

    def get_queryset(self):
        return self.queryset.filter(song_id=self.request.GET.get('song', None))
