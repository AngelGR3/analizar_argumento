from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models.base import Model
from django.forms import fields
from django.forms.models import ModelForm, model_to_dict
from core.models import usuario

class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True) 
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    escuela = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    sexo = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    fecha_cumple = forms.DateField(label="", widget=forms.DateTimeInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class' : 'text-muted f-w-400'}), required=True, )
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class' : 'text-muted f-w-400'}), required=True, )
   
    class Meta:
         model = usuario
         fields = ['username', 'first_name', 'last_name', 'escuela', 'sexo', 'fecha_cumple', 'email', 'password1', 'password2']
         help_text = { k:"" for k in fields}


class UpDateForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True)
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400'}), required=True) 
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400', 'placeholder': 'Apellido'}), required=True)
    escuela = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400', 'placeholder': 'Escuela'}), required=True)
    sexo = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'text-muted f-w-400', 'placeholder': 'Sexo'}), required=True)
    fecha_cumple = forms.DateField(label="", widget=forms.DateTimeInput(attrs={'class' : 'text-muted f-w-400', 'placeholder': 'Fecha de Nacimineto'}), required=True)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class' : 'text-muted f-w-400', 'placeholder': 'Correo'}), required=True)
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class' : 'text-muted f-w-400'}), required=True, )
   
    class Meta:
        model = usuario
        fields = ['username', 'first_name', 'last_name', 'escuela', 'sexo', 'fecha_cumple', 'email', 'password1']
        
 

    
    