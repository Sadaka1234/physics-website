from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from contenido.models import materia
from preguntas.models import ejercicio, ejercicio_usuario
from .forms import TopicoForm

context = dict()


@login_required(login_url='login')
def material(request):
  if request.method == 'POST':
    if "cerrar" in request.POST.keys():
      auth.logout(request)
      return redirect("login")

    elif "materia" in request.POST.keys():
      context["submaterias"]=materia.objects.filter(topico=request.POST["materia"]).values("subtopico").order_by().distinct()
      context["materia"]=request.POST["materia"]
      return render(request, 'eleccion-submaterial.html', context)

    elif "submateria" in request.POST.keys():
      actual = materia.objects.get(subtopico=request.POST["submateria"])
      context["preguntas"]= ejercicio.objects.filter(materia=actual.id)
      # Hay que crear el modelo de estudio context["preguntas"]=#
      context["submateria"] = request.POST["submateria"]
      return render(request, 'mostrar-material.html', context)

  context["materias"] = materia.objects.values("topico").order_by().distinct()
  return render(request, 'eleccion-material.html', context)
