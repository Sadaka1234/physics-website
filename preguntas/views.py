from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contenido.models import materia
from preguntas.models import ejercicio
from django.db.models import Max
import random

context = dict()

@login_required(login_url='login_view')
def pregunta(request):
  if request.method == "POST":
    if "certamen" in request.POST.keys():
      certamen = request.POST["certamen"]
      if certamen == "Todo":
        materias = materia.objects.all()
      else:
        materias = materia.objects.filter(topico=certamen)

      preguntas = get_pregunta(3, materias)
      print(preguntas)


  context["elecciones"] = [("Certamen 1: "," Oscilaciones, Ondas mecánicas y Sonido"),("Certamen Global: ","Todo")]
  return render(request, 'eleccion-certamen.html', context)


def get_pregunta(cantidad, topico):
  preguntas = []

  if topico == "Todo":
    max_id = ejercicio.objects.all().aggregate(max_id=Max("id"))['max_id']
    preguntas= ejercicio.objects.all()
  else:
    max_id = ejercicio.objects.filter(materia__topico__in=topico).aggregate(max_id=Max("id"))['max_id']
    preguntas= ejercicio.objects.filter(materia__topico__in=topico)

  while True:
    pk = random.randint(1, max_id)
    pregunta = preguntas.filter(pk=pk).first()

    if pregunta and pregunta not in preguntas:
      preguntas.append( pregunta )

    if len(preguntas) == cantidad:
      return preguntas


