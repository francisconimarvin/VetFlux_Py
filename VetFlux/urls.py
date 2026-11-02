from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tutores/", views.lista_tutores, name="lista_tutores"),
]