from django.shortcuts import render

from utils.blog.factory import make_post

# Create your views here.


def home(request):
    return render(request, 'blog/pages/home.html', context={
        'blogs': [make_post() for _ in range(10)],
    })


def blog(request, id):
    return render(request, 'blog/pages/post_view.html', context={
        'blog': make_post(),
        'is_detail_page': True,
    })
