from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from  inicio.models import SuperHeroe
from django.shortcuts import render, redirect
from inicio.forms import CreacionSuperHeroeFormulario


# Create your views here.
def crear_superheroe(request):
    if request.method == "POST":
        formulario = CreacionSuperHereoFormulario(request.POST)
        
        if formulario.is_valid():
        # limita al usuario a colocar cosas que estan malas como en la edad
            datos_correctos = formulario.cleaned_data
            
            
            superheroe = SuperHeroe (nombre = request.POST['nombre'], superpoder = request.POST['superpoder'], motivo = request.POST['motivo'], autor = request.POST['autor'])
            superheroe.save()

            return redirect('listar_superheroe')
            
    formulario = CreacionSuperHereoFormulario()
    return render(request, 'inicio/crear_superheroe.html',{'formulario': formulario})


def lista_superheroe(request):
    return render(request, 'inicio/lista_superheroe.html')
