from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home.index"),
    path("lirr/", views.lirr, name="home.lirr"),
    path("mnr/", views.mnr, name="home.mnr"),
    path("<int:id>/", views.show, name="home.show"),
    path("<slug:page>/<slug:subpage>/", views.subpage, name="home.subpage"),
    path("refund/", views.refund, name="home.refund"),
    path("query/", views.query, name="home.query"),
    path("batches/", views.batches, name="home.batches"),
    path("deadbeat/", views.deadbeat, name="home.deadbeat"),
    path("list_deadbeats/", views.list_deadbeats, name="home.list_deadbeats"),
]
