from os import name
from ensayo.models import ensayo
from core.views import home
from django.urls import path
from django.urls.resolvers import URLPattern
from ensayo.views import vista_ensayo, lista_ensayo

URLPattern = [
  path('ensayo', vista_ensayo, name=ensayo),
]