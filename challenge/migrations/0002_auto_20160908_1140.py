# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-08 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='challenge.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='images/user_images/nothing.jpg', upload_to='images/user_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='member',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Tag'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='acronym',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='image',
            field=models.ImageField(default='images/organization_images/nothing.jpg', upload_to='images/organization_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Tag'),
        ),
        migrations.AlterField(
            model_name='project',
            name='detail_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='geo_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='geo_y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='images/project_images/nothing.jpg', upload_to='images/project_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sponsoring_organizations',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Organization'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Tag'),
        ),
        migrations.AlterField(
            model_name='project',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Team'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Tag'),
        ),
        migrations.AlterField(
            model_name='role',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='hrs_per_week',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(blank=True, default='images/tag_images/nothing.jpg', null=True, upload_to='images/tag_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='team',
            name='acronym',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='images/team_images/nothing.jpg', upload_to='images/team_images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='challenge.Tag'),
        ),
    ]
