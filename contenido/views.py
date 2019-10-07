from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from contenido.models import materia, estudio, estudio_usuario
from preguntas.models import ejercicio

context = dict()

@login_required(login_url='login')
def material(request):
  if request.method == 'POST':
    if "materia" in request.POST.keys():
      consulta = request.POST.getlist('materia')
      context["submaterias"] = materia.objects.filter(topico__in=consulta).values("subtopico").order_by("topico","subtopico").distinct()
      context["materia"] = consulta
      return render(request, 'eleccion-submaterial.html', context)

    elif "submateria" in request.POST.keys():
      consulta = request.POST.getlist('submateria')
      materias = materia.objects.filter(topico__in=context["materia"], subtopico__in=consulta).order_by().distinct()
      id_materia = []
      for i in materias:
        id_materia.append(i)
      context["preguntas"] = ejercicio.objects.filter(materia__in=id_materia).values("ruta", "materia__subtopico").order_by("materia__topico","materia__subtopico").distinct()
      context["estudios"] = estudio.objects.filter(materia__in=id_materia).all().order_by().distinct()
      context["submateria"] = consulta
      return render(request, 'mostrar-material.html', context)

    elif "estudio-leido" in request.POST.keys():
      usuario = request.user
      study = estudio.objects.get(pk=request.POST["estudio-leido"])
      print(createUserEstudio(usuario, study))
      print(request.POST["ruta-leido"])
      return redirect(request.POST["ruta-leido"])


  context["materias"] = materia.objects.values("topico").order_by().distinct()
  return render(request, 'eleccion-material.html', context)


def createUserEstudio(username, estudio):
  value = estudio_usuario(usuario=username, estudio=estudio)
  try:
    value.save()
    print("Value saved in estudio_usuario")
    return True
  except:
    print("Already exists, we go on")
    return False




