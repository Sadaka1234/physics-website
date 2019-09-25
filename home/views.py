from django.shortcuts import render
import datetime

# Create your views here.
context = dict()
context["hora"]=datetime.datetime.now()
def main(request):
    return render(request, 'main.html', context)

def idem(request):
    return render(request, 'idem.html', context)

def login(request):
  return render(request, 'login.html', context)
