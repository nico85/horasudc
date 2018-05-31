# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0021_auto_20180305_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docentehoras',
            name='resolucion_anio',
            field=models.CharField(max_length=10, verbose_name=b'Resoluci\xc3\xb3n a\xc3\xb1o'),
        ),
        migrations.AlterField(
            model_name='docentehoras',
            name='resolucion_numero',
            field=models.CharField(max_length=40, verbose_name=b'Resoluci\xc3\xb3n n\xc3\xbamero'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='legajo_numero',
            field=models.IntegerField(unique=True, verbose_name=b'Legajo n\xc3\xbamero'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=b'Tel\xc3\xa9fono'),
        ),
        migrations.AlterField(
            model_name='personahoras',
            name='hs_catedras',
            field=models.IntegerField(verbose_name=b'Horas c\xc3\xa1tedras'),
        ),
        migrations.AlterField(
            model_name='personahoras',
            name='resolucion_anio',
            field=models.CharField(max_length=4, verbose_name=b'Resoluci\xc3\xb3n a\xc3\xb1o'),
        ),
        migrations.AlterField(
            model_name='personahoras',
            name='resolucion_numero',
            field=models.IntegerField(verbose_name=b'Resoluci\xc3\xb3n n\xc3\xbamero'),
        ),
    ]
