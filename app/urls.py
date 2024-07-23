from app.views import *
from django.urls import path

# from . import views


urlpatterns = [
    path("", home_page, name="home"),
    path("register/", register_page, name="register"),
]
