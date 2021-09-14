from gettingstarted.settings import LOGOUT_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from django.views.generic import edit
from ensayo.models import ensayo
from ensayo.form import EnsayoForm
from django.conf.urls import include, url
from django.contrib.auth.forms import UserCreationForm
#from ensayo.views import EnsayoCreate
from os import name
from django.urls import path
from django.urls import re_path


from django.contrib import admin
#from django.contrib.auth.views import login, logout

#views de nuestras apps
from core import views
from ensayo.views import  editar_ensayo, lista_ensayo, vista_ensayo, alizar
#from ensayo.views import EnsayoCreate


#admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
      path("", views.home, name="home"),
      #path("ensayo", EnsayoCreate.as_view(), name="ensayo"),
      path("admin/", admin.site.urls),
      path("registro", views.UsuarioRegistro.as_view(), name='registro'),
      path('accounts/', include('django.contrib.auth.urls')),
      #path('', include('social_django.urls', namespace='social')),
      path("ensayo/", login_required(vista_ensayo), name='ensayo' ),
      path("ensayos/",login_required(lista_ensayo), name='ensayos'),
      re_path("miperfil/(?P<pk>\d+)/",login_required(views.editar_usuario.as_view()), name='miperfil'),
      #re_path("editar/(?P<id_ensayo>\d+)/", editar_ensayo, name='editar_ensayo'),
      path("editarusuario/<int:id_ensayo>", editar_ensayo, name='editar_ensayo'),
     # path("analizarensayo/<int:id_ensayo>", alizar, name='analizar_ensayo'),
      path("analizarensayo/", alizar, name='analizar_ensayo'),
      
]
 