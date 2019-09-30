from django.conf.urls import url,include
from preguntas.views import *

urlpatterns = [
  url(r"^pregunta/$", pregunta, name="pregunta"),
]
