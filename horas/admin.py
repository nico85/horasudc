from django.contrib import admin
from horas.models import Sede, Carrera, Plan, Periodo, Materia,  \
    PersonalTipo, Personal, PersonalHoras, DocenteHoras
    #DocenteTipo

# Register your models here.

admin.site.register(Sede)
admin.site.register(Carrera)
admin.site.register(Plan)
admin.site.register(Periodo)
admin.site.register(Materia)
#admin.site.register(DocenteTipo)
admin.site.register(PersonalTipo)
admin.site.register(Personal)
admin.site.register(PersonalHoras)
admin.site.register(DocenteHoras)
