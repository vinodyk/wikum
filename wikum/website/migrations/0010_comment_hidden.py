# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_history_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
