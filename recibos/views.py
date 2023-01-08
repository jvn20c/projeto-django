from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, 'recibos/inicio.html', context={
        'nome': 'João Victor',
    })


def contato(request):
    return render(request=request, template_name='recibos/contato.html')


def sobre(request):
    return HttpResponse('/sobre: página sobre!')
