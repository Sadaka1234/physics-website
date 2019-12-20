from django.conf.urls import url,include
from preguntas.views import *

urlpatterns = [
  url(r"^pregunta/$", pregunta, name="pregunta"),
  url(r"^certamen/$", display_certamen, name="certamen"),
]
