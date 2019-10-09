# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20191009_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(default=b'Description will be placed here', null=True),
        ),
    ]
