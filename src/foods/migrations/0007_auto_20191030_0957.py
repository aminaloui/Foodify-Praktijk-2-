# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20191029_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
