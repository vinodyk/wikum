# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-27 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_tag_tagcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagcomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='tagcomment',
            name='tag',
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(to='website.Tag'),
        ),
        migrations.DeleteModel(
            name='TagComment',
        ),
    ]
