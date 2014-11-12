# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='public_token',
            field=models.CharField(max_length=64, null=True),
            preserve_default=True,
        ),
    ]
