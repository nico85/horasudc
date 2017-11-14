# -*- coding: utf-8 -*-
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

    personas = todas_las_personas
    cantPersonas = len(todas_las_personas)

    if request.method == 'GET':

        if len(todas_las_personas) > 0:

            '''paginator = Paginator(todas_las_personas, 20)  # Show 20 contacts per page
    
            page = request.GET.get('page', 1)
    
            try:
                personas = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                personas = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                personas = paginator.page(paginator.num_pages)
            '''
            return render(request, 'personasList.html', {
                #'page': page,
                #'paginator': paginator,
                'personas': personas,
                'grupo': grupo,
                'docentes': docentes,
                'administrativos': administrativos,
                'cantPersonas': cantPersonas,
                'estadoSel': -1
            })
        else:
            return render(request, 'personasList.html', {
                'personas': personas,
                'grupo': grupo,
                'docentes': docentes,
                'administrativos': administrativos,
                'cantPersonas': cantPersonas,
            })
    else:
        estadoSel = -1
        if 'estado' in request.POST and int(request.POST['estado']) > -1:
            personas = personas.filter(activo=request.POST['estado'])
            estadoSel = int(request.POST['estado'])
        cantPersonas = len(personas)
        return render(request, 'personasList.html', {
            # 'page': page,
            # 'paginator': paginator,
            'personas': personas,
            'grupo': grupo,
            'docentes': docentes,
            'administrativos': administrativos,
            'cantPersonas': cantPersonas,
            'estadoSel': estadoSel
        })

@login_required()
def personasNew(request):
    lista_sexo = ['Femenino', 'Masculino']
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/personas/')
        else:
            return render(request, 'personasNew.html', {
                'form': form,
                'sexos': lista_sexo,
            })
    else:
        form = PersonaForm()
        return render(request, 'personasNew.html', {
            'form': form,
            'sexos': lista_sexo,
        })


@login_required()
def personasEdit(request, pid):
    persona = get_object_or_404(Persona, id=pid)
    lista_sexo = ['Femenino', 'Masculino']
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('/personas/')
        else:
            return render(request, 'personasEdit.html', {
                'persona': persona,
                'form': form,
                'sexos': lista_sexo,
            })
    else:
        form = PersonaForm(instance=persona)
        return render(request, 'personasEdit.html', {
            'persona': persona,
            'form': form,
            'sexos': lista_sexo,
        })

@login_required()
def consadm(request):
    ANIOS = ('2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009',)
    adms = PersonaHoras.objects.all().order_by('-fecha_fin')
    total_adms = adms.count()
    dependencias = Dependencia.objects.all()
    anioSel = '0'
    dependenciaSel = '0'
    fechaDesdeSel = ''
    fechaHastaSel = ''

    global gbl_cons_adm
    gbl_cons_adm = adms

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
            anioSel = request.POST['anio']
        if 'dependencia' in request.POST and int(request.POST['dependencia']) > 0:
            adms = adms.filter(dependencia_id=request.POST['dependencia'])
            dependenciaSel = int(request.POST['dependencia'])
        if 'fecha_desde' in request.POST and request.POST['fecha_desde'] != "":
            fechaDesdeSel = request.POST['fecha_desde']
            if 'fecha_hasta' in request.POST and request.POST['fecha_hasta'] != "":
                # ejemplo: Order.objects.filter(drop_off__gte=start_date, pick_up__lte=end_date)
                adms = adms.filter(fecha_inicio__gte=request.POST['fecha_desde'], fecha_fin__lte=request.POST['fecha_hasta'])
                fechaHastaSel = request.POST['fecha_hasta']
            else:
                adms = adms.filter(fecha_inicio__gte=request.POST['fecha_desde'])
        else:
            if 'fecha_hasta' in request.POST and request.POST['fecha_hasta'] != "":
                adms = adms.filter(fecha_fin__lte=request.POST['fecha_hasta'])
                fechaHastaSel = request.POST['fecha_hasta']

        #global gbl_cons_adm
        gbl_cons_adm = adms

        return render(request, 'consultaadministrativo.html', {
            'administrativos': adms,
            'dependencias': dependencias,
            'anios': ANIOS,
            'dependencia': dependencia,
            'anio': anio,
            'total_adms': total_adms,
            'anioSel': anioSel,
            'dependenciaSel': dependenciaSel,
            'fechaDesdeSel': fechaDesdeSel,
            'fechaHastaSel': fechaHastaSel
        })


@login_required()
def consdoc(request):
    ANIOS = ('2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009',)
    sedes = Sede.objects.all()
    carreras = Carrera.objects.all()
    docs = DocenteHoras.objects.all()
    total_docs = docs.count()
    sedeSel = 0
    carreraSel = 0
    anioSel = '0'
    fechaDesdeSel = ''
    fechaHastaSel = ''

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

    global gbl_cons_doc
    gbl_cons_doc = docs

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
            sedeSel = int(request.POST['sede'])
        if 'carrera' in request.POST and int(request.POST['carrera']) > 0:
            docs = docs.filter(materia__plan__carrera_id=request.POST['carrera'])
            carreraSel = int(request.POST['carrera'])
        if 'anio' in request.POST and int(request.POST['anio']) > 0:
            docs = docs.filter(resolucion_anio=request.POST['anio'])
            anioSel = request.POST['anio']
        if 'fecha_desde' in request.POST and request.POST['fecha_desde'] != "":
            fechaDesdeSel = request.POST['fecha_desde']
            if 'fecha_hasta' in request.POST and request.POST['fecha_hasta'] != "":
                # ejemplo: Order.objects.filter(drop_off__gte=start_date, pick_up__lte=end_date)
                docs = docs.filter(fecha_inicio__gte=request.POST['fecha_desde'], fecha_fin__lte=request.POST['fecha_hasta'])
                fechaHastaSel = request.POST['fecha_hasta']
            else:
                docs = docs.filter(fecha_inicio__gte=request.POST['fecha_desde'])
        else:
            if 'fecha_hasta' in request.POST and request.POST['fecha_hasta'] != "":
                docs = docs.filter(fecha_fin__lte=request.POST['fecha_hasta'])
                fechaHastaSel = request.POST['fecha_hasta']

        #global gbl_cons_doc
        gbl_cons_doc = docs

        return render(request, 'consultadocente.html', {
            'docentes': docs,
            'sedes': sedes,
            'carreras': carreras,
            'anios': ANIOS,
            'total_docs': total_docs,
            'lista_hs': lista_hs,
            'sedeSel': sedeSel,
            'carreraSel': carreraSel,
            'anioSel': anioSel,
            'fechaDesdeSel': fechaDesdeSel,
            'fechaHastaSel': fechaHastaSel,
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
    # obtener el Arreglo de años (actual al 2009)
    hoy = date.today()
    anio_actual = hoy.year
    nro_fil = (anio_actual - 2008)
    lista_anios = [None] * nro_fil
    i = 0
    for n in range(nro_fil):
        lista_anios[n] = anio_actual - i
        i += 1
    # Fin obtener el arreglo de años
    form = PersonaHorasForm()
    persona = Persona.objects.get(id=pid)
    dependencias = Dependencia.objects.all()
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
                'anios': lista_anios,
                'dependencias': dependencias,
            })
    else:
        return render(request, 'personasHorasNew.html', {
            'persona': persona,
            'form': form,
            'anios': lista_anios,
            'dependencias': dependencias,
        })

@login_required()
def personasHorasEdit(request, phid):
    pershoras = PersonaHoras.objects.get(id=phid)
    form = PersonaHorasForm(instance=pershoras)
    persona = Persona.objects.get(id=pershoras.persona_id)
    pid = persona.id
    # obtener el Arreglo de años (actual al 2009)
    hoy = date.today()
    anio_actual = hoy.year
    nro_fil = (anio_actual - 2008)
    lista_anios = [None] * nro_fil
    i = 0
    for n in range(nro_fil):
        lista_anios[n] = anio_actual - i
        i += 1
    # Fin obtener el arreglo de años
    dependencias = Dependencia.objects.all()
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
                'anios': lista_anios,
                'dependencias': dependencias,
            })
    else:
        return render(request, 'personasHorasEdit.html', {
            'perhscat': pershoras,
            'persona': persona,
            'form': form,
            'anios': lista_anios,
            'dependencias': dependencias,
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
    lista_remunerado = ['Remunerado', 'Ad Honorem']
    # obtener el Arreglo de años (actual al 2009)
    hoy = date.today()
    anio_actual = hoy.year
    nro_fil = (anio_actual - 2008)
    lista_anios = [None] * nro_fil
    i = 0
    for n in range(nro_fil):
        lista_anios[n] = anio_actual - i
        i += 1
    # Fin obtener el arreglo de años
    sedes = Sede.objects.all()
    carreras = Carrera.objects.all()
    materias = Materia.objects.all().order_by('plan__carrera_id','anio_academico','periodo_id')
    docenteTipos = TipoDocente.objects.all()
    form = DocenteHorasForm()
    persona = Persona.objects.get(id=pid)
    if request.method == 'POST':
        form = DocenteHorasForm(request.POST)
        if form.is_valid():
            mat = Materia.objects.get(id=request.POST['materia'])
            doc_tipo = TipoDocente.objects.get(id=request.POST['docente_tipo'])
            new_dochs = form.save(commit=False)
            new_dochs.persona_id = persona.id
            # new_dochs.fecha_inicio = mat.periodo.fecha_inicio
            # new_dochs.fecha_fin = mat.periodo.fecha_fin
            new_dochs.fecha_inicio = request.POST['fecha_inicio']
            new_dochs.fecha_fin = request.POST['fecha_fin']
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
            return render(request, 'docentesHorasNew.html', {
                'persona': persona,
                'form': form,
                'carreras': carreras,
                'sedes': sedes,
                'materias': materias,
                'remunerados': lista_remunerado,
                'docenteTipos': docenteTipos,
                'anios': lista_anios,
            })
    else:
        return render(request, 'docentesHorasNew.html', {
            'persona': persona,
            'form': form,
            'carreras': carreras,
            'sedes': sedes,
            'materias': materias,
            'remunerados': lista_remunerado,
            'docenteTipos': docenteTipos,
            'anios': lista_anios,
        })

@login_required()
def docenteHorasEdit(request, dhid):
    lista_remunerado = ['Remunerado', 'Ad Honorem']
    # obtener el Arreglo de años (actual al 2009)
    hoy = date.today()
    anio_actual = hoy.year
    nro_fil = (anio_actual - 2008)
    lista_anios = [None] * nro_fil
    i = 0
    for n in range(nro_fil):
        lista_anios[n] = str(anio_actual - i)
        i += 1
    # Fin obtener el arreglo de años
    sedes = Sede.objects.all()
    carreras = Carrera.objects.all()
    materias = Materia.objects.all()
    docenteTipos = TipoDocente.objects.all()
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
            #new_dochs.fecha_inicio = mat.periodo.fecha_inicio
            #new_dochs.fecha_fin = mat.periodo.fecha_fin
            new_dochs.fecha_inicio = request.POST['fecha_inicio']
            new_dochs.fecha_fin = request.POST['fecha_fin']
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
                'sedes': sedes,
                'carreras': carreras,
                'docenteTipos': docenteTipos,
                'materias': materias,
                'remunerados': lista_remunerado,
                'anios': lista_anios,
            })
    else:
        return render(request, 'docentesHorasEdit.html', {
            'dochoras': dochoras,
            'form': form,
            'sedes': sedes,
            'carreras': carreras,
            'docenteTipos': docenteTipos,
            'materias': materias,
            'remunerados': lista_remunerado,
            'anios': lista_anios,
        })

@login_required()
def export_admin_xls(request):
    administrativos = gbl_cons_adm
    hoy = date.today()
    dia = hoy.day
    mes = hoy.month
    anio = hoy.year
    str_fecha = str(anio)+'-'+str(mes)+'-'+str(dia)
    response = HttpResponse(content_type='text/csv', charset='utf-8')
    response['Content-Disposition'] = 'attachment; filename="' + str_fecha +'_consulta_horas_catedras.xlsx"'

    writer = csv.writer(response)
    writer.writerow(['Apellido y Nombre', 'CUIL', 'Resolucion', 'Fecha Inicio', 'Fecha Fin', 'Hs_catedras', 'Dependencia'])

    for adm in administrativos:
        apenom = (adm.persona.apellidos + ', ' + adm.persona.nombres).encode('ascii', 'replace')
        depend = (adm.dependencia.dependencia_nombre).encode('ascii', 'replace')
        resolu = str(adm.resolucion_numero) + '/' + str(adm.resolucion_anio)
        writer.writerow([apenom, adm.persona.cuil, resolu, adm.fecha_inicio, adm.fecha_fin, adm.hs_catedras, depend])

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
    response['Content-Disposition'] = 'attachment; filename="' + str_fecha +'_consulta_horas_docentes.xlsx"'

    writer = csv.writer(response)
    writer.writerow(['Apellido y Nombre', 'Sede', 'Carrera', 'Materia', 'Resolucion', 'Fecha Inicio', 'Fecha Fin', 'Horas Materia',
                     'Hs total materia', 'Hs a liquidar', 'Anio academico', 'Periodo'])

    for doc in docentes:
        apenom = (doc.persona.apellidos + ', ' + doc.persona.nombres).encode('ascii', 'replace')
        resolu = str(doc.resolucion_numero) + '/' + str(doc.resolucion_anio)
        tot_pocentaje = (doc.porcentaje_aplicado * doc.materia.hs_semanales) / 100
        tot = doc.materia.hs_semanales + doc.hs_institucionales + tot_pocentaje
        writer.writerow(
            [apenom, doc.sede.sede_nombre.encode('ascii', 'replace'), doc.materia.plan.carrera.carrera_nombre.encode('ascii', 'replace')
                , doc.materia.materia_nombre.encode('ascii', 'replace'), resolu, doc.fecha_inicio,
             doc.fecha_fin, doc.materia.hs_semanales, doc.materia.hs_total_materia, tot,
             doc.materia.anio_academico, doc.materia.periodo.periodo_nombre.encode('ascii', 'replace')]
        )

    return response