# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20170729_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
