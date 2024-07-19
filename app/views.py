from django.shortcuts import render
from django.conf import settings
from .models import *

# Create your views here.


def home_page(request):
    return render(request, "base.html")
