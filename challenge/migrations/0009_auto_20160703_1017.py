# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_auto_20160702_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='Organization',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.ImageField(upload_to='images/tag_images/%Y/%m/%d', blank=True, null=True),
        ),
    ]
