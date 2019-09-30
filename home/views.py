from django.shortcuts import render, redirect
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
context = dict()
context["hora"]=datetime.datetime.now()
def main(request):
    return render(request, 'main.html', context)

def idem(request):
    return render(request, 'idem.html', context)

def login(request):
  if request.method == 'POST':
    if ("username" in request.POST.keys()) and ("password" in request.POST.keys()):
      user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
      if user is not None and user.is_active:
        auth.login(request, user)
        return redirect("main")
      else:
        context["error"]="Revisar usuario o contraseña"
        return render(request, 'login.html', context)
  return render(request, "login.html", context)

@login_required(login_url='')
def vista_logueado(request):
  return render(request, "main.html", context)
