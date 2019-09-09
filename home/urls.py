from django.conf.urls import url,include
from home.views import *

urlpatterns = [
  url(r"^$",main,name="main"),
  url(r"^idem/$", idem, name="idem"),
]
