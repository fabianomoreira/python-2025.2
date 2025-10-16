from django.shortcuts import render
from django.http import HttpResponse
from visitantes.models import Visitante

def index(request):
    total_visitantes = Visitante.objects.all()
  
    context = {
        'nome_pagina': 'Início da Dashboard',
        'total_visitantes': total_visitantes
    }

    return render(request, "index.html", context)
