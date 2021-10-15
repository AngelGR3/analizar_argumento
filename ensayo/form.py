from django import forms
from ensayo.models  import ensayo

class EnsayoForm(forms.ModelForm):
    class Meta :
        model = ensayo
        exclude = ['usuario']
        fields=[
            'titulo', 'materia', 'texto', 'usuario',  'mar_premisa', 'mar_conclu', 'mar_valorpremisa', 'mar_valorconclu', 'numparrafos', 'promedio',
        ]

        labels= {
             
             'titulo': '',  'materia': '', 'texto': '',  'mar_premisa': '', 'mar_conclu' : '', 'mar_volorpremsis': '', 'mar_valorconclu' : '','numparrafos' : '', 'promedio' : ''

        }

        widgets= {
            
            'titulo': forms.TextInput({ 'class' : 'in ', 'value': 'Titulo', 'id':'titulo' }),
            'materia': forms.TextInput({'class' : 'in', 'value': 'Materia', 'id':'materia'}),
            'texto': forms.Textarea({'class' : 'in2','placeholder': 'Ingresa tu texto','id':'texto', 'cols':'110', 'rows' : '20'}),
            'mar_premisa': forms.TextInput({ 'class' : 'in premisa', 'placeholder': ' ',  'id' : 'premisa'}),
            'mar_conclu': forms.TextInput({ 'class' : 'in conclusion', 'placeholder': ' ', 'id' : 'conclu'}),
            'mar_valorpremisa': forms.Textarea({ 'class' : 'in3 premisa', 'placeholder': ' ', 'id' : 'mar_valorpremisa','cols':'20', 'rows' : '7'}),
            'mar_valorconclu': forms.Textarea({ 'class' : 'in3 conclusion', 'placeholder': ' ', 'id' : 'mar_valorconclu','cols':'20', 'rows' : '7' }),
            'numparrafos': forms.TextInput({ 'class' : 'in', 'placeholder': ' ', 'id' : 'numparrafos'}),
            'promedio' : forms.TextInput({'class' : 'in', 'placeholder' : ' ', 'id' : 'promedio'}),

        }