# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0012_auto_20160915_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='stories',
            field=models.ManyToManyField(blank=True, to='challenge.Story'),
        ),
    ]
