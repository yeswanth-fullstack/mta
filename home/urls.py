from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home.index"),
    path("lirr/", views.lirr, name="home.lirr"),
    path("mnr/", views.mnr, name="home.mnr"),
    path("<int:id>/", views.show, name="home.show"),
    path("<slug:page>/<slug:subpage>/", views.subpage, name="home.subpage"),
]
