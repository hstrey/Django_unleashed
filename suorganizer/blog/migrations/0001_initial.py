# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(unique_for_month='pub_date', max_length=63, help_text='A label for URL config')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date published', auto_now_add=True)),
                ('startups', models.ManyToManyField(related_name='blog_posts', to='organizer.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='organizer.Tag')),
            ],
            options={
                'get_latest_by': 'pub_date',
                'verbose_name': 'blog post',
                'ordering': ['-pub_date', 'title'],
            },
        ),
    ]
