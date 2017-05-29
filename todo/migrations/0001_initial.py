# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
