from django.urls import path
from . import views



app_name = 'blogs'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/category/<int:category_id>/', views.category, name="category"),
    path('posts/<int:id>/', views.blog, name="blog"),
]
