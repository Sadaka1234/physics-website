from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from contenido.models import *
from preguntas.models import *
from home.forms import SignUpForm
from django.utils.translation import activate
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
  topicos = materia.objects.all().values('topico').order_by().distinct()
  context['perfil'] = dict()
  for topico in topicos:
    topico = topico['topico']
    preguntas = ejercicio_usuario.objects.filter(usuario=request.user, ejercicio__materia__topico=topico).values('ejercicio__ruta','resuelto').order_by().distinct()
    if preguntas:
      context['perfil'][topico] = []
      for pregunta in preguntas:
        (context['perfil'][topico]).append((pregunta['ejercicio__ruta'],pregunta['resuelto']))

    if context['perfil'] == {}:
      context['perfil']["No has resuelto preguntas! Es un buen momento para ponerte a estudiar! :D"] = []


  return render(request, 'profile.html', context)
