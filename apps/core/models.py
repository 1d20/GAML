from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Song(models.Model):
    singer = models.ForeignKey(Singer)
    title = models.CharField(max_length=255, default='')

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

    def __unicode__(self):
        return str(self.site) + ': ' + self.media_url + ' | ' + self.song_text


class Comment(models.Model):
    song = models.ForeignKey(Song)
    content = models.TextField()
    email = models.EmailField()

    def __unicode__(self):
        return str(self.song) + ': ' + self.content
