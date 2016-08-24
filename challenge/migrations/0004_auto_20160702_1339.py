# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_auto_20160702_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Organization',
            name='image',
            field=models.ImageField(upload_to='appchallenge/static/images/organization_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(upload_to='appchallenge/static/images/user_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='appchallenge/static/images/project_images/%Y/%m/%d'),
        ),
    ]
