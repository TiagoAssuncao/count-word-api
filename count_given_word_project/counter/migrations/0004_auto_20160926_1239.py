# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_auto_20160926_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
