from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Blog


def home(request):
    blogs = Blog.objects.filter(
        is_published=True
    ).order_by('-id')
    
    return render(request, 'blog/pages/home.html', context={
        'blogs': blogs,
        'title': 'WebDocs'
    })

def category(request, category_id):
    # Busca os blogs da categoria especificada, publicados, ordenados do mais recente para o mais antigo
    blogs = get_list_or_404(Blog.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id'))
    
    return render(request, 'blog/pages/category.html', context={
        'blogs': blogs,
        'title': f'Categoria-{blogs[0].category.name}'
    })

def blog(request, id):
    blog_post = get_object_or_404(Blog, id=id, is_published=True)
    
    return render(request, 'blog/pages/post_view.html', context={
        'blog': blog_post,
        'is_detail_page': True,
    })
