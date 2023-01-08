from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'recibos/inicio.html')

def contato(request):
    return HttpResponse('/contato: página de CONTATO!')

def sobre(request):
    return HttpResponse('/sobre: página sobre!')    