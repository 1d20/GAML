# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('singer', models.ForeignKey(to='core.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='SongInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site', models.IntegerField(choices=[(1, b'Site1'), (2, b'Site2'), (3, b'Site3')])),
                ('media_url', models.CharField(max_length=255, null=True, blank=True)),
                ('media_info', models.CharField(max_length=255, null=True, blank=True)),
                ('song_text', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
