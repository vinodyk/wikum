# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-10 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_article_comment_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary_num',
            field=models.IntegerField(default=0),
        ),
    ]