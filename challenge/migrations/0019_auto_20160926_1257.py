# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-26 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0018_auto_20160916_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='geo_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='geo_y',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='geo_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='geo_y',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='geo_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='geo_y',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='geo_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='geo_y',
            new_name='longitude',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='geo_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='geo_y',
            new_name='longitude',
        ),
    ]
