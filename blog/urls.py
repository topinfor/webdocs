from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/<int:id>/', views.blog, name="blog"),
]
