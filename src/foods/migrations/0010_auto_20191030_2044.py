# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0009_food_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='media',
            field=models.FileField(null=True, upload_to=b'download_media_location', blank=True),
        ),
    ]
