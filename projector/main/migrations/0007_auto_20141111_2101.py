# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20141111_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 0, 46, 664691), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 0, 55, 487287), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 1, 3, 255046), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskestimate',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 1, 6, 262989), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskestimate',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 21, 1, 8, 613005), auto_now=True),
            preserve_default=False,
        ),
    ]
