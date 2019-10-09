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
        materias = ejercicio.objects.all().distinct()
      else:
        materias = ejercicio.objects.filter(materia__topico=certamen).all()
      context['certamen'] = get_pregunta(3, materias)
      return redirect(display_certamen)
  context["elecciones"] = [("Certamen 1: ","Oscilaciones, Ondas mecánicas y Sonido"),("Certamen Global: ","Todo")]
  return render(request, 'eleccion-certamen.html', context)


def get_pregunta(cantidad, preguntas):
  output = []
  max_id = preguntas.all().aggregate(max_id=Max("id"))['max_id']

  while True:
    pk = random.randint(1, max_id)
    pregunta = preguntas.filter(pk=pk).first()

    if len(output) == cantidad:
      return output

    if pregunta and (pregunta not in output):
      output.append( pregunta )


@login_required(login_url='login_view')
def display_certamen(request):
  if "certamen" in context.keys():
    for i in context["certamen"]:
     return render(request, 'mostrar-certamen.html', context)
  else:
    return redirect(pregunta)



