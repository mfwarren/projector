# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskestimate',
            name='is_na',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
