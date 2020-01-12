from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from contenido.models import *
from preguntas.models import *
from home.forms import SignUpForm
from django.utils.translation import activate
import os

activate('es')

# Create your views here.
context = dict()


@login_required(login_url='login_view')
def main(request):
  return render(request, 'main.html', context)


@login_required(login_url='login_view')
def logout(request):
  auth.logout(request)
  return redirect("login_view")


@login_required(login_url='login_view')
def idem(request):
  return render(request, 'idem.html', context)


def login_view(request):
  if request.method == 'POST':
    if ("username" in request.POST.keys()) and ("password" in request.POST.keys()):
      user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
      if user is not None and user.is_active:
        auth.login(request, user)
        return redirect("main")
      else:
        context["error"] = "Revisar usuario o contraseña"
        return render(request, 'login.html', context)
  if request.user.is_authenticated:
    return redirect("main")
  return render(request, "login.html", context)


def signup(request):
  if request.user.is_authenticated:
    return redirect("main")
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('main')
    else:
      context['form'] = form
      return render(request, "signup.html", context)
  context['form'] = SignUpForm()
  return render(request, "signup.html", context)


@login_required(login_url="login_view")
def profile(request):
  #print(dir(request.user))
  topicos = materia.objects.all().values('topico').order_by("ejercicio__nombre").distinct()
  context['perfil'] = dict()
  context['estudios'] = dict()
  for topico in topicos:
    topico = topico['topico']
    context['certamenes'] = certamen.objects.filter(usuario=request.user).order_by("fecha")
    #preguntas = ejercicio_usuario.objects.filter(usuario=request.user, ejercicio__materia__topico=topico).values('ejercicio__ruta','resuelto').order_by("ejercicio__nombre").distinct()
    estudios = estudio_usuario.objects.filter(usuario=request.user, estudio__materia__topico=topico).values("estudio__ruta", "estudio__nombre", "estudio__estudio_usuario__fecha").order_by("estudio__nombre").distinct()
    #if preguntas:
    #  context['perfil'][topico] = []
    #  for pregunta in preguntas:
    #    (context['perfil'][topico]).append((pregunta['ejercicio__ruta'],pregunta['resuelto']))
    if estudios:
      context['estudios'][topico] = []
      for estudio in estudios:
        (context['estudios'][topico]).append((estudio["estudio__nombre"], estudio['estudio__ruta'], estudio["estudio__estudio_usuario__fecha"]))
  if context['certamenes'] == {}:
    context['certamenes']['No se han guardado certamenes. Genera uno y guardalo!'] = []

  #if context['perfil'] == {}:
  #  context['perfil']["No has resuelto preguntas! Es un buen momento para ponerte a estudiar! :D"] = []
  if context['estudios'] == {}:
    context['estudios']["No se ha leido nada! Más vale empezar a estudiar ;3"] = []
  return render(request, "profile.html", context)
