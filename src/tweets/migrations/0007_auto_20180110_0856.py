# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-10 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20180102_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
