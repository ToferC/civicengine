# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0014_auto_20160916_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.TextField(max_length=255),
        ),
    ]
