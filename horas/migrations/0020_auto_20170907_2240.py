# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0019_auto_20170907_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(max_length=20),
        ),
    ]
