# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-18 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_comment_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='vectorizer',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
