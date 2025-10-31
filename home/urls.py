from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home.index"),
    path("mnr/", views.mnr, name="home.mnr"),
]
