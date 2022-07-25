from django.shortcuts import render
from django.http import HttpResponse
from familia.models import Familia

# Create your views here.

def agregar(request):
    familia=Familia(nombre="Maria Agustina Flores", edad="20", nacimiento="2002-04-16")
    familia.save()
    familia=Familia(nombre="Juan Portal", edad="25", nacimiento="2007-03-15")
    familia.save()
    familia=Familia(nombre="Jesus Avila", edad="28", nacimiento="2010-02-25")
    familia.save()
    return HttpResponse('Se cargaron registros..')

    

def listar(request):
    integrantes=Familia.objects.all()
    return render(request, "templates/list.html",{"integrantes": integrantes})