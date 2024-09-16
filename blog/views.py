from django.shortcuts import render
# from django.urls import path

# from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'blog/pages/home.html', context={
        'name': 'Banco de Conhecimento'
    })


def blog(request, id):
    return render(request, 'blog/pages/post_view.html', context={
        'name': 'Banco de Conhecimento'
    })
