import tkinter
root = tkinter.Tk()
from django import forms
from django.db.models.base import Model
from django.urls.resolvers import get_resolver
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from core.models import usuario
from core.forms import UpDateForm, UserRegisterForm


def home(request):
    return render(request, "home.html")

class UsuarioRegistro (CreateView):
    model= usuario
    form_class = UserRegisterForm
    template_name= "registro.html"
    success_url= reverse_lazy(home)

def miperfil(request):
    id = request.user.id
    perfil = usuario.objects.get(id = id)  
    form = UserRegisterForm()
    if request.method == 'GET':
        form = UserRegisterForm(instance=perfil)  
    else:
        form = UserRegisterForm(request.POST, instance=perfil)  
        if form.is_valid():
            form.save()
            return redirect(home)
         
        
    return render(request, 'usuariodetalles.html', {'form':form})    

def eliminar_usuario(request):
    id = request.user.id
    perfil = usuario.objects.get(id = id)  
    form = UserRegisterForm()
    if request.method == 'GET':
        form = UserRegisterForm(instance=perfil)  
    if request.method == 'POST' :
        perfil.delete()
        return redirect ('')

    return render(request, 'eliminarusuario.html', {'form':form})         
    













