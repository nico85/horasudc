from django.contrib.admin.utils import model_format_dict
from django.db import models

# Create your models here.

class Version(models.Model):
    version_sistema = models.CharField(max_length=8)

    def __str__(self):
        return self.version_sistema

class Cambio(models.Model):
    version = models.ForeignKey(Version)
    detalle = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.detalle

class Sede (models.Model):
    sede_nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.sede_nombre

class Carrera (models.Model):
    carrera_nombre = models.CharField(max_length=230, unique=True)
    carrera_abreviada = models.CharField(max_length=10, unique=True, blank=True, null=True)
    sedes = models.ManyToManyField(Sede)

    class Meta:
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.carrera_nombre

class Plan (models.Model):
    carrera = models.ForeignKey(Carrera)
    plan_nombre = models.CharField(max_length=50)
    plan_version = models.IntegerField(blank=True, null=True, default=1)
    resolucion_fecha = models.DateField(blank=True, null=True)
    resolucion_numero = models.IntegerField(blank=True, null=True)
    total_horas = models.IntegerField(blank=True, null=True)
    cant_materias = models.IntegerField(blank=True, null=True, default=0)
    cant_materias_optativas = models.IntegerField(blank=True, null=True, default=0)
    cant_materias_idiomas = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.plan_nombre

class Periodo (models.Model):
    periodo_nombre = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return self.periodo_nombre


class Materia (models.Model):
    materia_nombre = models.CharField(max_length=400)
    plan = models.ForeignKey(Plan)
    hs_semanales = models.IntegerField(null=True)
    hs_total_materia = models.IntegerField(null=True)
    anio_academico = models.IntegerField(null=True)
    periodo = models.ForeignKey(Periodo)

    class Meta:
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.materia_nombre

class TipoDocente (models.Model):
    tipo_docente = models.CharField(max_length=50)
    porcentaje_aplicado = models.IntegerField(null=True)
    hs_institucionales = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Tipo de Docente'

    def __str__(self):
        return self.tipo_docente

class Persona (models.Model):
    cuil = models.CharField('C.U.I.L.', max_length=11, unique=True)
    apellidos = models.CharField('Apellido/s', max_length=40)
    nombres = models.CharField('Nombre/s', max_length=40)
    sexo = models.CharField(max_length=20, default='Sin Especificar')
    legajo_numero = models.IntegerField('Legajo numero', unique=True)
    telefono = models.CharField('Telefono', max_length=30, blank=True, null=True,)
    email = models.EmailField('E-mail', blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=True, null=True,)
    antiguedad = models.IntegerField()
    activo = models.CharField(max_length=2, default='1')

    class Meta:
        ordering = ['apellidos']
        verbose_name_plural = 'Personas'

    def __str__(self):
        return '%s, %s' %(self.apellidos, self.nombres)

class Dependencia(models.Model):
    dependencia_nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Dependencias'

    def __str__(self):
        return self.dependencia_nombre

class PersonaHoras (models.Model):
    persona = models.ForeignKey(Persona)
    resolucion_numero = models.IntegerField('Resolucion numero')
    resolucion_anio = models.CharField('Resolucion anio', max_length=10)
    hs_catedras = models.IntegerField('Horas catedras')
    fecha_inicio = models.DateField('Fecha de Inicio')
    fecha_fin = models.DateField('Fecha de Fin')
    dependencia = models.ForeignKey(Dependencia)

    class Meta:
        verbose_name_plural = 'Persona-Horas'

class DocenteHoras (models.Model):
    persona = models.ForeignKey(Persona)
    materia = models.ForeignKey(Materia)
    sede = models.ForeignKey(Sede)
    docente_tipo = models.ForeignKey(TipoDocente)
    resolucion_numero = models.CharField('Resolucion numero', max_length=40)
    resolucion_anio = models.CharField('Resolucion anio', max_length=10)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    remunerado = models.CharField(max_length=30)
    porcentaje_aplicado = models.IntegerField(blank=True, null=True)
    hs_institucionales = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Docente-Horas'



