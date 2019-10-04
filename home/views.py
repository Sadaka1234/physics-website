from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from preguntas.models import *
from contenido.models import *

# Create your views here.
context = dict()

@login_required(login_url='login')
def main(request):
  if request.method == 'POST':
    if "cerrar" in request.POST.keys():
      auth.logout(request)
      return redirect("login")
  return render(request, 'main.html', context)


@login_required(login_url='login')
def idem(request):
  if request.method == 'POST':
    if "cerrar" in request.POST.keys():
      auth.logout(request)
      return redirect("login")
  return render(request, 'idem.html', context)

def login(request):
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
  return render(request, "signup.html", context)


@login_required()
def profile(request):
  if request.method == 'POST':
    if "cerrar" in request.POST.keys():
      auth.logout(request)
      return redirect("login")

  email = User.objects.filter(is_active=True).exclude(email='').values_list('email', flat=True)[0]
  context["email"] = email
  contenidos = materia.objects.all().values('topico').order_by().distinct()

  for i in contenidos:
    print(" o ")

  context["preguntas"] = "queso"
  return render(request, 'profile.html', context)

