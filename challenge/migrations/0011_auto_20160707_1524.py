# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenge', '0010_member_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('name_fr', models.CharField(null=True, max_length=128, blank=True)),
                ('acronym', models.CharField(max_length=128)),
                ('acronym_fr', models.CharField(null=True, max_length=128, blank=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('website', models.URLField(null=True, max_length=128, blank=True)),
                ('image', models.ImageField(upload_to='images/department_images/%Y/%m/%d')),
                ('geo_x', models.FloatField(null=True, blank=True)),
                ('geo_y', models.FloatField(null=True, blank=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='acronym_fr',
            field=models.CharField(null=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_fr',
            field=models.CharField(null=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='website',
            field=models.URLField(null=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(null=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='geo_x',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='geo_y',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(upload_to='images/user_images/%Y/%m/%d/%H_%M_%S'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.URLField(null=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='salary',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lab',
            name='tags',
            field=models.ManyToManyField(to='challenge.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='labs',
            field=models.ManyToManyField(to='challenge.Lab'),
        ),
    ]
