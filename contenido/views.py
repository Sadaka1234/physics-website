from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from contenido.models import materia, estudio, estudio_usuario
from preguntas.models import ejercicio
from .forms import TopicoForm
import os

context = dict()

@login_required(login_url='login')
def material(request):
  if request.method == 'POST':
    if "materia" in request.POST.keys():
      consulta = request.POST.getlist('materia')
      context["submaterias"] = materia.objects.filter(topico__in=consulta).values("subtopico").order_by().distinct()
      context["materia"] = consulta
      return render(request, 'eleccion-submaterial.html', context)

    elif "submateria" in request.POST.keys():
      consulta = request.POST.getlist('submateria')
      materias = materia.objects.filter(topico__in=context["materia"], subtopico__in=consulta).order_by().distinct()
      id_materia = []
      for i in materias:
        id_materia.append(i)
      context["preguntas"] = ejercicio.objects.filter(materia__in=id_materia).values("ruta", "materia__subtopico").order_by().distinct()
      context["estudios"] = estudio.objects.filter(materia__in=id_materia).values("ruta", "nombre").order_by().distinct()
      context["submateria"] = consulta
      return render(request, 'mostrar-material.html', context)

  context["materias"] = materia.objects.values("topico").order_by().distinct()
  return render(request, 'eleccion-material.html', context)
