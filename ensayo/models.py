from django.db import models
from django.contrib.auth.models import User

class ensayo(models.Model):
   
    id_ensayo = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    texto = models.CharField(max_length=10000)
    mar_premisa = models.CharField(max_length=100, default='0')
    mar_conclu = models.CharField(max_length=100, default='0')
    mar_valorpremisa = models.CharField(max_length=10000, default='0')
    mar_valorconclu = models.CharField(max_length=10000, default='0')
    numparrafos = models.IntegerField( default='0')
    promedio = models.CharField(max_length=100, default='0.0')
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
