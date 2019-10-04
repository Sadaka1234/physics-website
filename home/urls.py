from django.conf.urls import url,include
from home.views import *

urlpatterns = [
  url(r"^$",login,name="login"),
  url(r"^idem/$", idem, name="idem"),
  url(r"^main/$", main, name="main"),
  url(r"^profile/$", profile, name="profile"),
  url(r"^signup/$", signup, name="signup")
]
