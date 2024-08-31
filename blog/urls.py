from django.urls import path
from blog.views import home, sobre, contato


urlpatterns = [
    path('', home),  # type: ignore
    path('contato/', contato),
    path('sobre/', sobre),
]
