# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_comment_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_replacement',
            field=models.BooleanField(default=False),
        ),
    ]
