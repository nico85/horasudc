# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0014_auto_20170830_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='cant_materias',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='cant_materias_idiomas',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='cant_materias_optativas',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='total_horas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
