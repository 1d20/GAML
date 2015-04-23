from apps.core import models
from rest_framework import serializers, viewsets


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('song', 'content', 'email')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer


