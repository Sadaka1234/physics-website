from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

context = dict()

@login_required(login_url='login')
def pregunta(request):
  return render(request, 'pregunta.html', context)
