# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('name_fr', models.CharField(max_length=128)),
                ('acronym', models.CharField(max_length=128)),
                ('acronym_fr', models.CharField(max_length=128)),
                ('website', models.URLField(max_length=128)),
                ('image', models.ImageField(upload_to='organization_images/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('branch', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('phone', models.CharField(max_length=10)),
                ('profile', models.URLField(max_length=128)),
                ('image', models.ImageField(upload_to='user_images/%Y/%m/%d')),
                ('geo_x', models.FloatField()),
                ('geo_y', models.FloatField()),
                ('salary', models.IntegerField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('organization', models.ForeignKey(to='challenge.organization', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('short_text', models.TextField()),
                ('detail_text', models.TextField()),
                ('submitted_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='project_images/%Y/%m/%d')),
                ('geo_x', models.FloatField()),
                ('geo_y', models.FloatField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('role', models.CharField(max_length=64, choices=[('PM', 'Project Manager'), ('DS', 'Designer'), ('DV', 'Developer'), ('AN', 'Analyst'), ('CM', 'Communications'), ('PL', 'Project Lead'), ('CH', 'Champion'), ('SP', 'Project Support'), ('ST', 'Project Strategy')])),
                ('hrs_per_week', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('person', models.ForeignKey(to='challenge.Member')),
                ('project', models.ForeignKey(to='challenge.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('task', models.CharField(max_length=256)),
                ('duration', models.FloatField()),
                ('member', models.ForeignKey(to='challenge.Member')),
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
            model_name='project',
            name='team',
            field=models.ManyToManyField(to='challenge.Member', verbose_name='List of members'),
        ),
        migrations.AddField(
            model_name='member',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
    ]
