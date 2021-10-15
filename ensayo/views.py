from os import lseek, truncate
from typing import TextIO
from django.forms.models import model_to_dict
from django.http import request
from django.http import response
from django.http.response import JsonResponse
from django.contrib import messages

from django.urls.base import reverse
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import CreateView
from core import views
from core.models import usuario
from django.db.models.fields.related import ForeignKey
from django.template import Context, Template

from nltk import punkt, tokenize
import re  

import tkinter
root = tkinter.Tk()


from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from ensayo.models import ensayo
from ensayo.form import EnsayoForm

from core.views import home
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import get_list_or_404



def vista_ensayo(request):
        form = EnsayoForm() 
        patronPremisa = re.compile(r'ya que|puesto que|puesto|pues|como|en tanto que|dado que|viendo que|debido a|de acuerdo con|por cuanto|viendo que|a causa de|porque|se sigue de|como muestra|como es indicado por|la razón es que|se puede inferir de|se puede derivar de|se puede deducir de|en vista de que|debido a') 
        patronConcl = re.compile(r'por lo tanto|por ende|de ahí que|en consecuencia|por consiguiente|se desprende de|como resultado|llegamos a la conclusión|por lo tanto|por tanto|lo cual apunta a la conclusión de que|lo cual muestra que|así que|lo cual nos permite inferir que|correspondientemente|lo cual implica que|lo cual prueba que|lo cual significa que|se sigue que|por estas razones|por esta razón|podemos inferir que|concluyo que|consecuentemente')
        parrafos = 1
        indicaconclu = ''
        indicapremisa = ''
        if request.method == 'POST' :
            form= EnsayoForm(request.POST)
            if form.is_valid(): 
                form=form.save(commit=False)
                parrafos= (re.findall(r'((.+)\w+)', form.texto, re.U))
                form.numparrafos = len(parrafos)
                premisaentexto = patronPremisa.findall(form.texto.lower())
                concluentexto = patronConcl.findall(form.texto.lower())

                if patronConcl.findall(form.texto.lower()):
                    for conclutexto2 in concluentexto:
                        if conclutexto2 in concluentexto:
                            indicaconclu = conclutexto2+ ", " + indicaconclu
                            form.mar_valorconclu = indicaconclu 
                else:
                    form.mar_valorconclu = '0'

                if patronPremisa.findall(form.texto.lower()):
                    for premisatexto2 in premisaentexto:
                        if premisatexto2 in premisaentexto:
                            indicapremisa = premisatexto2+ ", " + indicapremisa
                            form.mar_valorpremisa = indicapremisa
                else:
                    form.mar_valorpremisa = '0'    
                
                form.mar_premisa= len(premisaentexto)
                form.mar_conclu= len(concluentexto)
                if form.mar_premisa > 0 or form.mar_conclu > 0:
                    promedio = ((len(premisaentexto) + len(concluentexto)) / len(parrafos))
                    
                    if promedio <= 1.69:
                        promediolim = round(promedio,2)
                        form.promedio = str(promediolim),"Arg./Baja" 
                    if 1.10<= promedio <=1.70:
                        promediolim = round(promedio,2)
                        form.promedio = str(promediolim),"Arg./Media"
                    if promedio >= 1.8:
                        promediolim = round(promedio,2)
                        form.promedio = str(promediolim),"Arg./Alta"
                else:
                    form.promedio = '0.0'  
       
                form.usuario = request.user
               
                #form.save()
                data = {'premisa': form.mar_premisa, 'conclu' : form.mar_conclu, 'mar_valorpremisa' : form.mar_valorpremisa, 'mar_valorconclu' : form.mar_valorconclu, 'numparrafos' : form.numparrafos, 'promedio' : form.promedio}
                return JsonResponse(data)
            else:
                print("hay un erro ")

        return render(request, 'crear_ensayo.html', {'form':form})

def save(request):
    form = EnsayoForm() 
    
    if request.method == 'POST' :
            form= EnsayoForm(request.POST)
            if form.is_valid(): 
               
                form=form.save(commit=False)
                form.usuario = request.user 
                messages.success(request, " ")
                form.save()
               
                return redirect (home)
            else:
                print("hay un erro ")

    return render(request, 'crear_ensayo.html', {'form':form})      
    

def lista_ensayo (request):
    lista = ensayo.objects.filter(usuario_id= request.user)
    contexto = {'ensayos': lista}
    return render(request, 'lista_ensayo.html', contexto  )


def editar_ensayo(request, id_ensayo):
    editar = ensayo.objects.get(id_ensayo = id_ensayo)  
    if request.method == 'GET':
        form = EnsayoForm(instance=editar)  
    else:
        form = EnsayoForm(request.POST, instance=editar)  
        if form.is_valid():
            messages.success(request, "Ensayo editado")
            form.save()
            return redirect ('/ensayos')
        
    return render(request, 'crear_ensayo.html', {'form':form})         
    

def eliminar_ensayo(request, id_ensayo):
    registro = ensayo.objects.get(id_ensayo = id_ensayo)  
    if request.method == 'GET':
        form = EnsayoForm(instance=registro)  
    if request.method == 'POST' :
        registro.delete()
        messages.success(request, "Ensayo eliminado")
        return redirect ('/ensayos')

    return render(request, 'eliminar_ensayo.html', {'form':form})         
    
