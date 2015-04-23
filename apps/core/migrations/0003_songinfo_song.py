# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150423_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='songinfo',
            name='song',
            field=models.ForeignKey(default=1, to='core.Song'),
            preserve_default=False,
        ),
    ]
