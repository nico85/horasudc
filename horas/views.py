from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.views.generic.base import TemplateView
from horas.models import *

# Create your views here.

@login_required()
def inicio(request):
    return render(request, 'inicio.html')

@login_required()
def personal(request):
    personas = Personal.objects.all()
    return render(request, 'personal.html', {'personas': personas})

@login_required()
def consadm(request):
    adms = PersonalHoras.objects.all()
    return render(request, 'consultaadministrativo.html', {'administrativos': adms})

@login_required()
def consdoc(request):
    docs = DocenteHoras.objects.all()
    return render(request, 'consultadocente.html', {'docentes': docs})
