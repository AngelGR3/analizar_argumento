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
from ensayo.views import  editar_ensayo, lista_ensayo, vista_ensayo, save, eliminar_ensayo
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
      path("admin/", admin.site.urls),
      path("registro", views.UsuarioRegistro.as_view(), name='registro'),
      path('accounts/', include('django.contrib.auth.urls')),
      #path('', include('social_django.urls', namespace='social')),
      path("ensayo/", login_required(vista_ensayo), name='ensayo' ),
      path("save/", login_required(save), name='save' ),
      path("ensayos/",login_required(lista_ensayo), name='ensayos'),
   #   re_path("miperfil",login_required(views.miperfil), name='miperfil'),
      re_path("editar/(?P<id_ensayo>\d+)/", editar_ensayo, name='editar_ensayo'),
      re_path("eliminar/(?P<id_ensayo>\d+)/", eliminar_ensayo, name='eliminar_ensayo'),
      path("miperfil/", login_required(views.miperfil), name='miperfil'),
      path("eliminar_usuario/", login_required(views.eliminar_usuario), name='eliminar_usuario'),
      
]
 