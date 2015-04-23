from django.contrib import admin
from django.contrib.auth.models import Group, User
from . import models


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(models.Singer)
admin.site.register(models.Song)
admin.site.register(models.SongInfo)
admin.site.register(models.Comment)
