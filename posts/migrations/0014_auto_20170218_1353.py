# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-18 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_remove_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
