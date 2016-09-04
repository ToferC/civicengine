# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 00:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('name_fr', models.CharField(blank=True, max_length=128, null=True)),
                ('acronym', models.CharField(max_length=128)),
                ('acronym_fr', models.CharField(blank=True, max_length=128, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(upload_to='images/organization_images/%Y/%m/%d')),
                ('geo_x', models.FloatField(blank=True, null=True)),
                ('geo_y', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('profile', models.URLField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(upload_to='images/user_images/%Y/%m/%d/%H_%M_%S')),
                ('bio', models.TextField(blank=True, null=True)),
                ('geo_x', models.FloatField(blank=True, null=True)),
                ('geo_y', models.FloatField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenge.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('name_fr', models.CharField(blank=True, max_length=128, null=True)),
                ('acronym', models.CharField(max_length=128)),
                ('acronym_fr', models.CharField(blank=True, max_length=128, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(upload_to='images/organization_images/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('short_text', models.TextField()),
                ('detail_text', models.TextField()),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images/project_images/%Y/%m/%d')),
                ('geo_x', models.FloatField()),
                ('geo_y', models.FloatField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teams', models.ManyToManyField(to='challenge.Team')),
                ('sponsoring_organizations', models.ManyToManyField(to='challenge.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Project Manager', 'Project Manager'), ('Designer', 'Designer'), ('Developer', 'Developer'), ('Analyst', 'Analyst'), ('Communications', 'Communications'), ('Project Lead', 'Project Lead'), ('Champion', 'Champion'), ('Project Support', 'Project Support'), ('Project Strategy', 'Project Strategy')], max_length=64)),
                ('hrs_per_week', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Member')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/tag_images/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('task', models.CharField(max_length=256)),
                ('duration', models.FloatField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Member')),
                ('resources', models.ManyToManyField(blank=True, to='challenge.Resource')),
                ('tags', models.ManyToManyField(to='challenge.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='sprint',
            name='work',
            field=models.ManyToManyField(to='challenge.Work'),
        ),
        migrations.AddField(
            model_name='resource',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='member',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenge.Organization'),
        ),
        migrations.AddField(
            model_name='member',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
    ]
