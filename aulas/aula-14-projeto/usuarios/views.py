from django.shortcuts import render
from django.http import HttpResponse
from visitantes.models import Visitante
from porteiros.models import Porteiro

def index(request):
    total_visitantes = Visitante.objects.all()
    total_porteiros = Porteiro.objects.all()
  
    context = {
        'nome_pagina': 'Início da Dashboard',
        'total_visitantes': total_visitantes,
        'total_porteiros': total_porteiros
    }

    return render(request, "index.html", context)
