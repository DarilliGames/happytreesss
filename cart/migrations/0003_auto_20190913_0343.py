# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-13 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190912_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
