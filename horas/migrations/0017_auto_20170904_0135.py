# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0016_auto_20170830_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='materia_nombre',
            field=models.CharField(max_length=400),
        ),
    ]
