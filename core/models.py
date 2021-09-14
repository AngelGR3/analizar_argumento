from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class usuario (User):

    escuela = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    fecha_cumple = models.DateField()
    