from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("new/", views.new, name="new"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("random/", views.rnd, name="random"),
    path("wiki/<str:name>", views.page, name="page"),
]
