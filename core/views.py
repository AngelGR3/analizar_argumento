from django import forms
from django.db.models.base import Model
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

    


class editar_usuario (UpdateView):
    model= usuario
    form_class = UpDateForm
    template_name= "usuariodetalles.html"
    success_url= reverse_lazy(home)     













