from django import forms
from .models import Persona, PersonaHoras, DocenteHoras

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('apellidos', 'nombres', 'cuil', 'legajo_numero', 'telefono', 'email', 'fecha_nacimiento', 'cuil', 'sexo', 'activo', 'antiguedad')

class PersonaHorasForm(forms.ModelForm):

    class Meta:
        model = PersonaHoras
        fields = ('resolucion_numero', 'resolucion_anio', 'hs_catedras', 'fecha_inicio', 'fecha_fin', 'dependencia')

class DocenteHorasForm(forms.ModelForm):

    class Meta:
        model = DocenteHoras
        fields = ('resolucion_numero', 'resolucion_anio', 'remunerado', 'materia', 'sede', 'docente_tipo')
