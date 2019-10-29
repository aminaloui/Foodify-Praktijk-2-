# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(default=b'Description will be placed here', null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=100, decimal_places=2),
        ),
    ]
