# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-14 08:16
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170113_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]