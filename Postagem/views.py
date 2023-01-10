from django.shortcuts import render, redirect
from . import views
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')
