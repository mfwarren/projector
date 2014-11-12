# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141111_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='asdf', editable=False),
            preserve_default=False,
        ),
    ]
