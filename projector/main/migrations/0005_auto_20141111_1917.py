# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_project_public_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='actual_duration',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.CharField(max_length=64, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taskestimate',
            name='comments',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
