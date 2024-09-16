from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),  # type: ignore
    path('posts/<int:id>/', views.blog),
]
