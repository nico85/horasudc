from django.contrib import admin
from horas.models import Sede, Carrera, Plan, Periodo, Materia,  \
    TipoDocente, Persona, PersonaHoras, DocenteHoras, Dependencia, Version, Cambio

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'cuil', 'sexo', 'id')
    search_fields = ('apellidos', 'nombres')

class PersonaHorasAdmin(admin.ModelAdmin):
    list_display = ('persona', 'resolucion_numero', 'resolucion_anio', 'fecha_inicio', 'fecha_fin', 'hs_catedras')
    #search_fields = ('nombres', 'apellidos')

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('carrera_nombre',)
    search_fields = ('carrera_nombre',)
    filter_horizontal = ('sedes',)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('materia_nombre', 'plan', 'hs_semanales', 'anio_academico', 'periodo')
    search_fields = ('materia_nombre',)

class DocenteHorasAdmin(admin.ModelAdmin):
    list_display = ('persona', 'resolucion_numero', 'resolucion_anio', 'fecha_inicio', 'fecha_fin', 'persona_id')


admin.site.register(Sede)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Plan)
admin.site.register(Periodo)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(TipoDocente)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(PersonaHoras, PersonaHorasAdmin)
admin.site.register(DocenteHoras, DocenteHorasAdmin)
admin.site.register(Dependencia)
admin.site.register(Version)
admin.site.register(Cambio)
