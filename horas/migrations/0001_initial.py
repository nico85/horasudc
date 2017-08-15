# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_carrera', models.CharField(max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='DocenteHoras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comision', models.CharField(max_length=30)),
                ('resolucion_numero', models.CharField(max_length=40)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('remunerado', models.CharField(choices=[('Asalariado', 'Asalariado'), ('Ad Honorem', 'Ad Honorem')], default='Asalariado', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DocenteTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_docente', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_materia', models.CharField(max_length=100)),
                ('hs_semanales', models.IntegerField(null=True)),
                ('hs_total', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil', models.CharField(max_length=11)),
                ('apellido', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('legajo_numero', models.IntegerField()),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('antiguedad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonalHoras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolucion_numero', models.CharField(max_length=40)),
                ('hs_semanales', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Personal')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_personal', models.CharField(max_length=50)),
                ('porcentaje_aplicado', models.IntegerField(null=True)),
                ('hs_institucionales', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(max_length=50)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='personal',
            name='personal_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.PersonalTipo'),
        ),
        migrations.AddField(
            model_name='materia',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Periodo'),
        ),
        migrations.AddField(
            model_name='materia',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Plan'),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='docente_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.DocenteTipo'),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Materia'),
        ),
        migrations.AddField(
            model_name='docentehoras',
            name='personal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Personal'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='horas.Sede'),
        ),
    ]