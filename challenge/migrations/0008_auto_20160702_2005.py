# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0007_auto_20160702_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(max_length=64, choices=[('Project Manager', 'Project Manager'), ('Designer', 'Designer'), ('Developer', 'Developer'), ('Analyst', 'Analyst'), ('Communications', 'Communications'), ('Project Lead', 'Project Lead'), ('Champion', 'Champion'), ('Project Support', 'Project Support'), ('Project Strategy', 'Project Strategy')]),
        ),
    ]
