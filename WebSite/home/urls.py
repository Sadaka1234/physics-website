from django.conf.urls import url,include
from home.views import *

urlpatterns = [
  url(r"^$", login_view, name="login_view"),
  url(r"^idem/$", idem, name="idem"),
  url(r"^main/$", main, name="main"),
  url(r"^profile/$", profile, name="profile"),
  url(r"^signup/$", signup, name="signup"),
  url(r"^logout/$", logout, name="logout"),
]
