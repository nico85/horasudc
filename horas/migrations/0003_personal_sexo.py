# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0002_auto_20170813_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='sexo',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Mujer', max_length=20),
        ),
    ]
