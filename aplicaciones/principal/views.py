from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm


def inicio(request):
    personas = Persona.objects.all() #select * from Persona
    contexto = {
            'personas':personas
    }
    return render(request,'index.html',contexto)

def crearPersona(request):
    form = PersonaForm()
    contexto = {
        'form':form
    }
    return render(request,'crear_persona.html',contexto)
