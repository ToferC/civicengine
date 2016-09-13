# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-13 15:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20160912_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenge.Member'),
        ),
        migrations.AlterField(
            model_name='role',
            name='status',
            field=models.CharField(choices=[('Vacant', 'Vacant'), ('Applied', 'Applied'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Retired', 'Retired'), ('Removed', 'Removed')], default='Applied', max_length=64),
        ),
    ]
