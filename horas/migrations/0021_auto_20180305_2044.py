# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-05 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0020_auto_20170907_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='docentehoras',
            name='baja',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='motivo_baja',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='observaciones_baja',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='resolucion_anio_baja',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='resolucion_numero_baja',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personahoras',
            name='baja',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personahoras',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personahoras',
            name='motivo_baja',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='personahoras',
            name='observaciones_baja',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='personahoras',
            name='resolucion_anio_baja',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='personahoras',
            name='resolucion_numero_baja',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personahoras',
            name='resolucion_anio',
            field=models.CharField(max_length=4, verbose_name='Resolución año'),
        ),
    ]
