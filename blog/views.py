from django.shortcuts import render
# from django.urls import path
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return HttpResponse('contato')
