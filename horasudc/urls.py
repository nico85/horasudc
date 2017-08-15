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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from horas import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(pattern_name='inicio', permanent=False)),
    url(r'^inicio/$', views.inicio, name='inicio'),
    url(regex=r'^inicio/login/$', view=login, kwargs={'template_name': 'login.html'}, name='login'),
    url(regex=r'^inicio/logout/$', view=logout, kwargs={'next_page': '/inicio'}, name='logout'),
    url(r'^inicio/personal/$', views.personal),
    url(r'^inicio/docente/$', views.consdoc),
    url(r'^inicio/administrativo/$', views.consadm),

]
