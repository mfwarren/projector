# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_email', models.EmailField(max_length=75)),
                ('permission', models.CharField(max_length=32)),
                ('token', models.CharField(max_length=64)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hide_estimates', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('estimate_project', 'Estimate Project'), ('view_project', 'View Project'), ('owns_project', 'Owns Project')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('assignee', models.CharField(max_length=255)),
                ('is_enabled', models.BooleanField(default=True)),
                ('group', models.CharField(max_length=64)),
                ('actual_duration', models.FloatField()),
                ('project', models.ForeignKey(to='main.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskEstimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likely', models.FloatField()),
                ('minimum', models.FloatField()),
                ('maximum', models.FloatField()),
                ('curve', models.CharField(max_length=32, choices=[(b'no_idea', b'No Idea'), (b'certain', b'Certain'), (b'less_sure', b'Less Sure'), (b'very_unsure', b'Very Unsure')])),
                ('comments', models.TextField()),
                ('is_na', models.BooleanField()),
                ('task', models.ForeignKey(to='main.Task')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='invitation',
            name='project',
            field=models.ForeignKey(to='main.Project'),
            preserve_default=True,
        ),
    ]
