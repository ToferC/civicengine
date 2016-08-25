# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_remove_project_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sponsoring_organizations',
            field=models.ManyToManyField(to='challenge.organization'),
        ),
        migrations.AlterField(
            model_name='Organization',
            name='image',
            field=models.ImageField(upload_to='staticfiles/images/organization_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='staticfiles/images/project_images/%Y/%m/%d'),
        ),
    ]
