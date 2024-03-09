from django.urls import path
from .views import *



urlpatterns = [
    path("", myfunction, name='main'),
    path("about/", myabout, name='about'),
    path("login/", mylogin, name='login'),
    path("registaration/", myregistration, name='reg'),
    path("contact/", mycontact, name='contact'),
    path("adminhome/", adminhome, name='adminpage'),
    path("userhome/", userhome, name='homepage'),
    path("registration_view/", registration_view, name='registration_view'),
    path("login_view/", login_view, name='login_view')



 ]