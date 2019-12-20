from django.conf.urls import url,include
from contenido.views import *

urlpatterns = [
  url(r"^material/$", material, name="material"),
  url(r"^display_pregunta/$", display_pregunta, name="display_pregunta"),
]
