from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from contenido.models import materia
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
    elif "submateria" in request.POST.keys():
      context["mensaje"]="Buen trabajo, hiciste dos queries"
  else:
    form = TopicoForm()
  context["materias"] = materia.objects.values("topico").order_by().distinct()
  return render(request, 'material.html', context)
