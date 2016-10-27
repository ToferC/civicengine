# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-27 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0019_auto_20160926_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='issue_type',
            field=models.CharField(choices=[('Opportunity', 'Opportunity'), ('Challenge', 'Challenge')], default='Challenge', max_length=32),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(default='Occupation', max_length=64),
        ),
        migrations.AlterField(
            model_name='role',
            name='status',
            field=models.CharField(choices=[('Vacant', 'Vacant'), ('Applied', 'Applied'), ('Active', 'Active'), ('Inactive', 'Inactive'), ('Retired', 'Retired'), ('Removed', 'Removed')], default='Vacant', max_length=64),
        ),
    ]