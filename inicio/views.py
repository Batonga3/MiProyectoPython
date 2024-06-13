from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio(request):
    return HttpResponse("HOLAAAAA")

def template1(request):
    fecha = datetime.now()   
    datos = {
        "fecha": fecha,
    }
    return render(request, "template1.html", datos)