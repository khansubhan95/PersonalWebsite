# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-22 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20170114_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]
