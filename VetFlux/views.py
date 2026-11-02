from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Tutor


def index(request):
    return HttpResponse("Hello, world. You're at the VetFlux index.")


def lista_tutores(request):
    tutores = Tutor.objects.all()

    return render(request, "VetFlux/tutores/lista.html", {
        "tutores": tutores
    })