from django.shortcuts import render

# Create your views here.
def main(request):
  return render(request,'inicio.html')

def submenu(request):
  return render(request, 'submenu.html')
