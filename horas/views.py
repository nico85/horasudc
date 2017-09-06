from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from horas.forms import PersonaForm, PersonaHorasForm, DocenteHorasForm

from horas.models import *

import csv
import math

from datetime import date

# Create your views here.

gbl_cons_adm = [None]
gbl_cons_doc = [None]

@login_required()
def inicio(request):
    version = Version.objects.last()
    cambios = Cambio.objects.filter(version_id=version.id)
    return render(request, 'inicio.html', {
        'version': version,
        'cambios': cambios,
    })

@login_required()
def personasList(request):

    #grupo = request.user.groups.get()
    grupo = 'superusuario'
    todas_las_personas = Persona.objects.all().order_by('apellidos')
    docentes = DocenteHoras.objects.all()
    administrativos = PersonaHoras.objects.all()

    paginator = Paginator(todas_las_personas, 10)  # Show 10 contacts per page

    page = request.GET.get('page', 1)

    try:
        personas = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        personas = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        personas = paginator.page(paginator.num_pages)

    return render(request, 'personasList.html', {
        'page': page,
        'paginator': paginator,
        'personas': personas,
        'grupo': grupo,
        'docentes': docentes,
        'administrativos': administrativos,
    })

@login_required()
def personasNew(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personas/')
        else:
            return render(request, 'personasNew.html', {'form': form})
    else:
        form = PersonaForm()
        return render(request, 'personasNew.html', {'form': form})


@login_required()
def personasEdit(request, pid):
    persona = get_object_or_404(Persona, id=pid)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('/personas/')
        else:
            return render(request, 'personasEdit.html', {
                'persona': persona,
                'form': form,
            })
    else:
        form = PersonaForm(instance=persona)
        return render(request, 'personasEdit.html', {
            'persona': persona,
            'form': form,
        })

@login_required()
def consadm(request):
    ANIOS = ('2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009',)
    adms = PersonaHoras.objects.all().order_by('-fecha_fin')
    total_adms = adms.count()
    dependencias = Dependencia.objects.all()
    if request.method == 'GET':
        return render(request, 'consultaadministrativo.html', {
            'administrativos': adms,
            'dependencias': dependencias,
            'anios': ANIOS,
            'total_adms': total_adms,
        })
    else:
        adms = PersonaHoras.objects.all()
        anio = 0
        dependencia = 0
        if 'anio' in request.POST and int(request.POST['anio']) > 0:
            adms = adms.filter(resolucion_anio=request.POST['anio'])
        if 'dependencia' in request.POST and int(request.POST['dependencia']) > 0:
            adms = adms.filter(dependencia_id=request.POST['dependencia'])

        global gbl_cons_adm
        gbl_cons_adm = adms

        return render(request, 'consultaadministrativo.html', {
            'administrativos': adms,
            'dependencias': dependencias,
            'anios': ANIOS,
            'dependencia': dependencia,
            'anio': anio,
            'total_adms': total_adms,
        })


@login_required()
def consdoc(request):
    ANIOS = ('2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009',)
    sedes = Sede.objects.all()
    carreras = Carrera.objects.all()
    docs = DocenteHoras.objects.all()
    total_docs = docs.count()

    nro_fil = len(docs)
    lista_hs = [None] * nro_fil
    for n in range(nro_fil):
        lista_hs[n] = {'id_doc': 0, 'tot_hs': 0}
        i = 0
    for dh in docs:
        tot_pocentaje = (dh.porcentaje_aplicado * dh.materia.hs_semanales) / 100
        tot = math.ceil(dh.materia.hs_semanales + dh.hs_institucionales + tot_pocentaje)
        lista_hs[i]['id_doc'] = dh.id
        lista_hs[i]['tot_hs'] = int(tot)
        i += 1

    if request.method == 'GET':
        return render(request, 'consultadocente.html', {
            'docentes': docs,
            'sedes': sedes,
            'carreras': carreras,
            'anios': ANIOS,
            'total_docs': total_docs,
            'lista_hs': lista_hs,
        })
    else:
        docs = DocenteHoras.objects.all()
        anio = 0
        sede = 0
        carrera = 0
        if 'sede' in request.POST and int(request.POST['sede']) > 0:
            docs = docs.filter(sede=request.POST['sede'])
        if 'carrera' in request.POST and int(request.POST['carrera']) > 0:
            docs = docs.filter(materia__plan__carrera_id=request.POST['carrera'])
        if 'anio' in request.POST and int(request.POST['anio']) > 0:
            docs = docs.filter(resolucion_anio=request.POST['anio'])

        global gbl_cons_doc
        gbl_cons_doc = docs

        return render(request, 'consultadocente.html', {
            'docentes': docs,
            'sedes': sedes,
            'carreras': carreras,
            'anios': ANIOS,
            'total_docs': total_docs,
            'lista_hs': lista_hs,
        })

@login_required()
def personasHorasList(request, pid):
    perhscat = PersonaHoras.objects.filter(persona_id=pid).order_by("-fecha_inicio")
    persona = Persona.objects.get(id=pid)
    return render(request, 'personasHorasList.html', {
        'perhscat': perhscat,
        'persona': persona,
    })

@login_required()
def personasHorasNew(request, pid):
    if request.method == 'POST':
        form = PersonaHorasForm(request.POST)
        if form.is_valid():
            perhscat = PersonaHoras.objects.filter(persona_id=pid).order_by("-fecha_inicio")
            persona = Persona.objects.get(id=pid)
            new_perhs = form.save(commit=False)
            new_perhs.persona_id = persona.id
            new_perhs.save()
            return render(request, 'personasHorasList.html', {
                'perhscat': perhscat,
                'persona': persona,
            })
        else:
            form = PersonaHorasForm()
            persona = Persona.objects.get(id=pid)
            return render(request, 'personasHorasNew.html', {
                'persona': persona,
                'form': form,
            })
    else:
        form = PersonaHorasForm()
        persona = Persona.objects.get(id=pid)
        return render(request, 'personasHorasNew.html', {
            'persona': persona,
            'form': form,
        })

@login_required()
def personasHorasEdit(request, phid):
    pershoras = PersonaHoras.objects.get(id=phid)
    form = PersonaHorasForm(instance=pershoras)
    persona = Persona.objects.get(id=pershoras.persona_id)
    pid = persona.id
    if request.method == 'POST':
        form = PersonaHorasForm(request.POST, instance=pershoras)
        if form.is_valid():
            new_perhs = form.save(commit=False)
            new_perhs.persona_id = persona.id
            new_perhs.save()
            url = '/horascatedras/'+ str(persona.id) + '/lista/'
            return redirect(url)
    else:
        return render(request, 'personasHorasEdit.html', {
            'perhscat': pershoras,
            'persona': persona,
            'form': form,
        })

@login_required()
def personasHorasDelete(request, phid):
    pershoras = get_object_or_404(PersonaHoras, id=phid)
    url = '/horascatedras/' + int(phid) + '/lista/'
    if request.method == 'POST':
        pershoras.delete()
        return redirect(url)
    return render(request, url)

@login_required()
def docenteHorasList(request, pid):
    dochoras = DocenteHoras.objects.filter(persona_id=pid).order_by('-fecha_inicio')
    persona = Persona.objects.get(id=pid)

    nro_fil = len(dochoras)
    lista_hs = [None] * nro_fil
    for n in range(nro_fil):
        lista_hs[n] = {'id_doc': 0, 'tot_hs': 0}
    i = 0
    for dh in dochoras:
        tot_pocentaje = (dh.porcentaje_aplicado * dh.materia.hs_semanales)/100
        tot = math.ceil(dh.materia.hs_semanales + dh.hs_institucionales + tot_pocentaje)
        lista_hs[i]['id_doc'] = dh.id
        lista_hs[i]['tot_hs'] = int(tot)
        i += 1

    return render(request, 'docentesHorasList.html', {
        'dochoras': dochoras,
        'persona': persona,
        'lista_hs': lista_hs,
    })

@login_required()
def docenteHorasNew(request, pid):
    if request.method == 'POST':
        persona = Persona.objects.get(id=pid)
        form = DocenteHorasForm(request.POST)
        if form.is_valid():
            mat = Materia.objects.get(id=request.POST['materia'])
            doc_tipo = TipoDocente.objects.get(id=request.POST['docente_tipo'])
            new_dochs = form.save(commit=False)
            new_dochs.persona_id = persona.id
            new_dochs.fecha_inicio = mat.periodo.fecha_inicio
            new_dochs.fecha_fin = mat.periodo.fecha_fin
            new_dochs.porcentaje_aplicado = doc_tipo.porcentaje_aplicado
            new_dochs.hs_institucionales = doc_tipo.hs_institucionales
            new_dochs.save()
            dochoras = DocenteHoras.objects.filter(persona_id=pid)
            return render(request, 'docentesHorasList.html', {
                'dochoras': dochoras,
                'persona': persona,
                'pid': pid,
            })
        else:
            #form = DocenteHorasForm()
            #persona = Persona.objects.get(id=pid)
            return render(request, 'docentesHorasNew.html', {
                'persona': persona,
                'form': form,
            })
    else:
        form = DocenteHorasForm()
        persona = Persona.objects.get(id=pid)
        return render(request, 'docentesHorasNew.html', {
            'persona': persona,
            'form': form,
        })

@login_required()
def docenteHorasEdit(request, dhid):
    dochoras = DocenteHoras.objects.get(id=dhid)
    form = DocenteHorasForm(instance=dochoras)
    persona = Persona.objects.get(id=dochoras.persona.id)
    if request.method == 'POST':
        form = DocenteHorasForm(request.POST, instance=dochoras)
        if form.is_valid():
            mat = Materia.objects.get(id=request.POST['materia'])
            doc_tipo = TipoDocente.objects.get(id=request.POST['docente_tipo'])
            new_dochs = form.save(commit=False)
            new_dochs.persona_id = persona.id
            new_dochs.fecha_inicio = mat.periodo.fecha_inicio
            new_dochs.fecha_fin = mat.periodo.fecha_fin
            new_dochs.porcentaje_aplicado = doc_tipo.porcentaje_aplicado
            new_dochs.hs_institucionales = doc_tipo.hs_institucionales
            new_dochs.save()
            dochoras = DocenteHoras.objects.filter(persona_id=persona.id)
            url = '/horasdocentes/'+str(persona.id)+'/lista/'
            return redirect(url)
    else:
        return render(request, 'docentesHorasEdit.html', {
            'dochoras': dochoras,
            'form': form,
        })

@login_required()
def export_admin_xls(request):
    administrativos = gbl_cons_adm
    hoy = date.today()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    str_fecha = str(anio)+'-'+str(mes)+'-'+str(dia)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + str_fecha +'_consulta_horas_catedras.xls"'

    writer = csv.writer(response)
    writer.writerow(['Apellido y Nombre', 'CUIL', 'Resolucion', 'Hs_catedras', 'Dependencia'])

    for adm in administrativos:
        apenom = str(adm.persona.apellidos) + ', ' + str(adm.persona.nombres)
        resolu = str(adm.resolucion_numero) + '/' + str(adm.resolucion_anio)
        writer.writerow([apenom, adm.persona.cuil, resolu, adm.hs_catedras, adm.dependencia.dependencia_nombre])

    return response

@login_required()
def export_doc_xls(request):
    docentes = gbl_cons_doc
    hoy = date.today()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    str_fecha = str(anio)+'-'+str(mes)+'-'+str(dia)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + str_fecha +'_consulta_horas_docentes.xls"'

    writer = csv.writer(response)
    writer.writerow(['Apellido y Nombre', 'Sede', 'Carrera', 'Materia', 'Resolucion', 'Horas Materia',
                     'Hs total materia', 'Hs a liquidar', 'Anio academico', 'Periodo'])

    for doc in docentes:
        apenom = str(doc.persona.apellidos) + ', ' + str(doc.persona.nombres)
        resolu = str(doc.resolucion_numero) + '/' + str(doc.resolucion_anio)
        tot_pocentaje = (doc.porcentaje_aplicado * doc.materia.hs_semanales) / 100
        tot = doc.materia.hs_semanales + doc.hs_institucionales + tot_pocentaje
        writer.writerow(
            [apenom, doc.sede.sede_nombre, doc.materia.plan.carrera.carrera_nombre, doc.materia.materia_nombre,
             resolu, doc.materia.hs_semanales, doc.materia.hs_total_materia, tot, doc.materia.anio_academico,
             doc.materia.periodo.periodo_nombre]
        )

    return response