# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='data published')),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'get_latest_by': 'pub_date',
                'ordering': ['-pub_date'],
                'verbose_name': 'news article',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=31)),
                ('slug', models.SlugField(max_length=31, help_text='A label for URL config', unique=True)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
            ],
            options={
                'get_latest_by': 'founded_date',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=31, unique=True)),
                ('slug', models.SlugField(max_length=31, help_text='A label for URL config', unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
    ]
