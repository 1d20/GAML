# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('song', models.ForeignKey(to='core.Song')),
            ],
        ),
        migrations.AddField(
            model_name='singer',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
