from django.contrib import admin

#Se le da permiso al admin para poder entrar a los modelos.
# Register your models here.

from .models import *

admin.site.register(Usuario)

