# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-28 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
