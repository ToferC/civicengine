# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_auto_20160908_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='team',
        ),
        migrations.RemoveField(
            model_name='role',
            name='project',
        ),
        migrations.AddField(
            model_name='member',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Team'),
        ),
    ]
