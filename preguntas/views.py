from django.shortcuts import render, redirect
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

context = dict()

@login_required(login_url='login')
def pregunta(request):
  if "cerrar" in request.POST.keys():
    auth.logout(request)
    return redirect("login")
  return render(request, 'pregunta.html', context)

