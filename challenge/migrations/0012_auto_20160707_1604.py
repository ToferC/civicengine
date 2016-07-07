# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0011_auto_20160707_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='branch',
        ),
        migrations.AddField(
            model_name='member',
            name='lab',
            field=models.ForeignKey(null=True, to='challenge.Lab', blank=True),
        ),
    ]
