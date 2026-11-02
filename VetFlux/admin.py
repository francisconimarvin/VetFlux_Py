# Register your models here.
from django.contrib import admin
from .models import (
    Tutor,
    Paciente,
    Agenda,
    FichaMedica,
    Instrumentos,
    Inventario,
    Medicamentos,
    Receta
)

admin.site.register([
    Tutor,
    Paciente,
    Agenda,
    FichaMedica,
    Instrumentos,
    Inventario,
    Medicamentos,
    Receta
])