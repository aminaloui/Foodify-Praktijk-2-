# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20191026_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='slug',
            field=models.SlugField(default=b'slug-field'),
        ),
    ]
