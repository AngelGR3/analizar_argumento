from os import lseek
from typing import TextIO
from django.forms.models import model_to_dict
from django.http import request
from django.http import response
from django.http.response import JsonResponse


from django.urls.base import reverse
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.edit import CreateView
from core import views
from core.models import usuario
from django.db.models.fields.related import ForeignKey
from django.template import Context, Template

from nltk import punkt, tokenize
import re  




from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from ensayo.models import ensayo
from ensayo.form import EnsayoForm

from core.views import home
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import get_list_or_404

#vista crear y analizar ensayo 
def vista_ensayo(request):
        patronPremisa = re.compile(r'ya que|puesto que|puesto|pues|como|en tanto que|dado que|viendo que|debido a|de acuerdo con|por cuanto|viendo que|a causa de|porque|se sigue de|como muestra|como es indicado por|la razón es que|se puede inferir de|se puede derivar de|se puede deducir de|en vista de que|debido a') 
        patronConcl = re.compile(r'por lo tanto|por ende|de ahí que|en consecuencia|por consiguiente|se desprende de|como resultado|llegamos a la conclusión|por lo tanto|por tanto|lo cual apunta a la conclusión de que|lo cual muestra que|así que|lo cual nos permite inferir que|correspondientemente|lo cual implica que|lo cual prueba que|lo cual significa que|se sigue que|por estas razones|por esta razón|podemos inferir que|concluyo que|consecuentemente')
       
        if request.method == 'POST' and  request.is_ajax:
            form= EnsayoForm(request.POST)
            if form.is_valid(): 
                form=form.save(commit=False)
                premisaentexto = patronPremisa.findall(form.texto)
                concluentexto = patronConcl.findall(form.texto)
                form.mar_valorconclu = "0"
                for conclutexto2 in concluentexto:
                    form.mar_valorconclu = conclutexto2
                form.mar_valorconclu = form.mar_valorconclu     
                for premisatexto2 in premisaentexto:
                    form.mar_valorpremisa = premisatexto2
                form.mar_premisa= len(premisaentexto)
                form.mar_conclu= len(concluentexto)
                form.usuario = request.user
                #form.save()
                #resultados del analisis
                data = {'premisa': form.mar_premisa, 'conclu' : form.mar_conclu, 'mar_valorpremisa' : form.mar_valorpremisa, 'mar_valorconclu' : form.mar_valorconclu}
                return JsonResponse(data)
            else:
                print("hay un erro ")

           
        form = EnsayoForm()        
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
            form.save()
        
    return render(request, 'crear_ensayo.html', {'form':form})         
    


def alizar (request):
    patronPremisa = re.compile(r'ya que|puesto que|puesto|pues|como|en tanto que|dado que|viendo que|debido a|de acuerdo con|por cuanto|viendo que|a causa de|porque|se sigue de|como muestra|como es indicado por|la razón es que|se puede inferir de|se puede derivar de|se puede deducir de|en vista de que|debido a') 
    patronConcl = re.compile(r'por lo tanto|por ende|de ahí que|en consecuencia|por consiguiente|se desprende de|como resultado|llegamos a la conclusión|por lo tanto|por tanto|lo cual apunta a la conclusión de que|lo cual muestra que|así que|lo cual nos permite inferir que|correspondientemente|lo cual implica que|lo cual prueba que|lo cual significa que|se sigue que|por estas razones|por esta razón|podemos inferir que|concluyo que|consecuentemente')
    ensayo1 = ensayo.objects.last()
    if request.method == 'GET':
        form = EnsayoForm(instance=ensayo1)
        premisaentexto = patronPremisa.findall(ensayo1.texto)
        concluentexto = patronConcl.findall(ensayo1.texto)
        for conclutexto2 in concluentexto:
            conclu = conclutexto2
            break    
        for premisatexto2 in premisaentexto:
            prem = premisatexto2
            break  

    else:
        form = EnsayoForm(request.POST, instance=ensayo1)  
        if form.is_valid():
            form.save()    
    
    return render(request, 'crear_ensayo.html', {'form':form, 'marcadoresconclu': conclu, 'marcadorespremisa' : prem})     





