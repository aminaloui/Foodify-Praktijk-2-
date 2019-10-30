# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_food_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='media',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
