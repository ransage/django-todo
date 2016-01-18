# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('body', models.TextField(blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField()),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('priority', models.PositiveIntegerField()),
                ('assigned_to', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='todo_assigned_to')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_by')),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(editable=False, max_length=60)),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(to='todo.List'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='todo.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together=set([('group', 'slug')]),
        ),
    ]
