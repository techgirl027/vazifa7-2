from django.shortcuts import render
from django.conf import settings
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home_page(request):
    return render(request, "index.html")


def register_page(request):
    email = request.POST["email"]
    password = request.POST["password"]
    models.Contact.objects.create(email=email, password=password)
    return render(request, "login-register.html")


def login(request):
    # username = request.POST["username"]
    # password = request.POST["password"]
    # models.Contact.objects.create(username=username, password=password)
    return render(request, "login-register.html")
