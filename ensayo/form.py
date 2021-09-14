from django import forms
from ensayo.models  import ensayo

class EnsayoForm(forms.ModelForm):
    class Meta :
        model = ensayo
        exclude = ['usuario']
        fields=[
            'titulo', 'materia', 'texto', 'usuario',  'mar_premisa', 'mar_conclu', 'mar_valorpremisa', 'mar_valorconclu'
        ]

        

        labels= {
             
             'titulo': '',  'materia': '', 'texto': '',  'mar_premisa': '', 'mar_conclu' : '', 'mar_volorpremsis': '', 'mar_valorconclu' : ''

        }

        widgets= {
            
            'titulo': forms.TextInput({ 'class' : 'in', 'placeholder': 'Titulo', }),
            'materia': forms.TextInput({'class' : 'in', 'placeholder': 'Materia',}),
            'texto': forms.Textarea({'class' : 'in','placeholder': 'Ingresa tu texto', 'id':'texto', 'cols':'50', 'rows':'10' }),
            'mar_premisa': forms.TextInput({ 'class' : 'in premisa', 'placeholder': ' ', 'id' : 'premisa'}),
            'mar_conclu': forms.TextInput({ 'class' : 'in conclusion', 'placeholder': ' ', 'id' : 'conclu'}),
            'mar_valorpremisa': forms.TextInput({ 'class' : 'in premisa', 'placeholder': ' ', 'id' : 'mar_valorpremisa'}),
            'mar_valorconclu': forms.TextInput({ 'class' : 'in conclusion', 'placeholder': ' ', 'id' : 'mar_valorconclu'})

        }