"""
URL configuration for agenda_eventos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from lista.views import (EventosPorMesView,
                         EventosDoMesView,
                         EventosCreateView,
                         EventosUpdateView,
                         EventosDeleteView,
                         SolicitarDadosView,
                         EncerrarSessaoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', EventosPorMesView.as_view(), name='eventos_por_mes'),
    path('create/', EventosCreateView.as_view(), name='eventos_create'),
    path('eventos/<int:ano>/<int:mes>/', EventosDoMesView.as_view(), name='eventos_do_mes'),
    path('edicao/<int:pk>/', EventosUpdateView.as_view(), name='eventos_edicao'),
    path('delete/<int:pk>/', EventosDeleteView.as_view(), name='eventos_delete'),

    #Section
    path("", SolicitarDadosView.as_view(), name='lista_section'),
    path("encerra_sessao", EncerrarSessaoView.as_view(), name='lista_section_fim')
]