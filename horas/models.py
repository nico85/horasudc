from django.db import models

# Create your models here.

class Sede (models.Model):
    nombre_sede = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.nombre_sede

class Carrera (models.Model):
    nombre_carrera = models.CharField(max_length=230)
    sede = models.ForeignKey(Sede)

    class Meta:
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.nombre_carrera

class Plan (models.Model):
    carrera = models.ForeignKey(Carrera)
    nombre_plan = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.nombre_plan

class Periodo (models.Model):
    periodo = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Periodos'

    def __str__(self):
        return self.periodo

#class DocenteTipo (models.Model):
#    tipo_docente = models.CharField(max_length=40)

#    class Meta:
#        verbose_name_plural = 'Tipos de Docentes'

#    def __str__(self):
#        return self.tipo_docente

class Materia (models.Model):
    nombre_materia = models.CharField(max_length=100)
    plan = models.ForeignKey(Plan)
    periodo = models.ForeignKey(Periodo)
    hs_semanales = models.IntegerField(null=True)
    hs_total = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Materias'

    def __str__(self):
        return self.nombre_materia

class PersonalTipo (models.Model):
    tipo_personal = models.CharField(max_length=50)
    porcentaje_aplicado = models.IntegerField(null=True)
    hs_institucionales = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Tipos de Personal'

    def __str__(self):
        return self.tipo_personal

class Personal (models.Model):
    cuil = models.CharField(max_length=11)
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    legajo_numero = models.IntegerField()
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField('e-mail', blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    personal_tipo = models.ForeignKey(PersonalTipo)
    antiguedad = models.IntegerField()

    class Meta:
        ordering = ['apellido']
        verbose_name_plural = 'Personal'

    def __str__(self):
        return '%s, %s' %(self.apellido, nombre)

class PersonalHoras (models.Model):
    personal = models.ForeignKey(Personal)
    resolucion_numero = models.CharField(max_length=40)
    hs_semanales = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name_plural = 'Personal-Horas'

class DocenteHoras (models.Model):
    ASALARIADO = 'Asalariado'
    ADHONOREM = 'Ad Honorem'
    ARRAY_REMUNERADO = (
        (ASALARIADO, 'Asalariado'),
        (ADHONOREM, 'Ad Honorem'),
    )
    personal = models.ForeignKey(Personal)
    materia = models.ForeignKey(Materia)
    comision = models.CharField(max_length=30)
    #docente_tipo = models.ForeignKey(DocenteTipo)
    resolucion_numero = models.CharField(max_length=40)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    remunerado = models.CharField(
        max_length=30,
        choices=ARRAY_REMUNERADO,
        default=ASALARIADO,
    )

    class Meta:
        verbose_name_plural = 'Docente-Horas'



