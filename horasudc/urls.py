"""horasudc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.views import login, logout
from horas import views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    url(r'^horas/admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(pattern_name='inicio', permanent=False)),
    url(r'^horas/inicio/$', views.inicio, name='inicio'),
    url(regex=r'^horas/inicio/login/$', view=login, kwargs={'template_name': 'login.html'}, name='login'),
    url(regex=r'^horas/inicio/logout/$', view=logout, kwargs={'next_page': '/inicio'}, name='logout'),
    url(r'^horas/personas/$', views.personasList),
    url(r'^horas/docentes/$', views.consdoc),
    url(r'^horas/administrativos/$', views.consadm),
    url(r'^horas/personas/nueva/$', views.personasNew),
    url(r'^horas/personas/(?P<pid>[0-9]+)/editar/$', views.personasEdit),
    url(r'^horas/horascatedras/(?P<pid>[0-9]+)/lista/$', views.personasHorasList),
    url(r'^horas/horascatedras/(?P<pid>[0-9]+)/asignar/$', views.personasHorasNew),
    url(r'^horas/horascatedras/(?P<phid>[0-9]+)/editar/$', views.personasHorasEdit),
    url(r'^horas/horasdocentes/(?P<pid>[0-9]+)/lista/$', views.docenteHorasList),
    url(r'^horas/horasdocentes/(?P<pid>[0-9]+)/asignar/$', views.docenteHorasNew),
    url(r'^horas/horasdocentes/(?P<dhid>[0-9]+)/editar/$', views.docenteHorasEdit),
    url(r'^horas/admin/export/xls/$', views.export_admin_xls, name='export_admin_xls'),
    url(r'^horas/doc/export/xls/$', views.export_doc_xls, name='export_doc_xls'),
]
