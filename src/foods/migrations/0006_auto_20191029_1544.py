# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_auto_20191029_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(default=b'', null=True),
        ),
    ]
