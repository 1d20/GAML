from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField()

    def get_serialize_object(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def __unicode__(self):
        return self.name


class Song(models.Model):
    singer = models.ForeignKey(Singer)
    title = models.CharField(max_length=255, default='')

    def get_serialize_object(self):
        return {
            'id': self.id,
            'singer': self.singer.get_serialize_object(),
            'title': self.title
        }

    def __unicode__(self):
        return self.singer.name + ': ' + self.title


class SongInfo(models.Model):

    SITES_CHOICES = (
        (1, 'Site1'),
        (2, 'Site2'),
        (3, 'Site3'),
    )

    song = models.ForeignKey(Song)
    site = models.IntegerField(choices=SITES_CHOICES)
    media_url = models.CharField(max_length=255, null=True, blank=True)
    media_info = models.CharField(max_length=255, null=True, blank=True)
    song_text = models.CharField(max_length=255, null=True, blank=True)

    def get_serialize_object(self):
        return {
            'id': self.id,
            'song': self.song.get_serialize_object(),
            'media_url': self.media_url,
            'media_info': self.media_info,
            'song_text': self.song_text,
        }

    def __unicode__(self):
        return str(self.site) + ': ' + self.media_url + ' | ' + self.song_text


class Comment(models.Model):
    song = models.ForeignKey(Song)
    content = models.TextField()
    email = models.EmailField()

    def get_serialize_object(self):
        return {
            'id': self.id,
            'song': self.song.get_serialize_object(),
            'content': self.content,
            'email': self.email,
        }

    def __unicode__(self):
        return str(self.song) + ': ' + self.content
