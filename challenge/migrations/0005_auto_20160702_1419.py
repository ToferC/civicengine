# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_auto_20160702_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Organization',
            name='image',
            field=models.ImageField(upload_to='images/organization_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(upload_to='images/user_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/project_images/%Y/%m/%d'),
        ),
    ]
