# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-25 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=60),
        ),
    ]
