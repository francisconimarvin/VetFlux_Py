from datetime import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from .models import (
    Paciente,
    Tutor,
    Agenda,
    Inventario, 
    FichaMedica,
    Receta
    )

from .forms import (
    PacienteForm,
    TutorForm,
    AgendaForm,
    InventarioForm,
    FichaMedicaForm,
    RecetaForm
)

# Login
from django.contrib.auth.decorators import login_required



@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'login.html')

@never_cache
@login_required
def home(request):
    doctor = request.user.doctor
    pacientes = Paciente.objects.filter(doctor_fk=doctor).values('nombre', 'especie')
    return render(request, 'home.html', {
        'pacientes': list(pacientes),
    })

############
#PACIENTE

@never_cache
@login_required
def paciente(request):
    return render(request, 'paciente/index.html')

@never_cache
@login_required
def paciente_lista(request):
    doctor = request.user.doctor
    pacientes = Paciente.objects.filter(doctor_fk=doctor)
    return render(request, 'paciente/lista.html', {'pacientes': pacientes})

@never_cache
@login_required
def paciente_crear(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = PacienteForm(request.POST, doctor=doctor)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.doctor_fk = doctor
            paciente.save()
            return redirect('paciente_lista')
    else:
        form = PacienteForm(doctor=doctor)
    return render(request, 'paciente/form.html', {'form': form})

@never_cache
@login_required
def paciente_editar(request, pk):
    doctor = request.user.doctor
    paciente = get_object_or_404(Paciente, pk=pk, doctor_fk=doctor)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente, doctor=doctor)
        if form.is_valid():
            form.save()
            return redirect('paciente_lista')
    else:
        form = PacienteForm(instance=paciente, doctor=doctor)
    return render(request, 'paciente/form.html', {'form': form})

@never_cache
@login_required
def paciente_eliminar(request, pk):
    doctor = request.user.doctor
    paciente = get_object_or_404(Paciente, pk=pk, doctor_fk=doctor)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_lista')
    return render(request, 'paciente/confirmar_eliminar.html', {'paciente': paciente})





############
#TUTOR

@never_cache
@login_required
def tutor(request):
    return render(request, 'tutor/index.html')

@never_cache
@login_required
def tutor_lista(request):
    doctor = request.user.doctor
    tutores = Tutor.objects.filter(doctor_fk=doctor)
    return render(request, 'tutor/lista.html', {'tutores': tutores})

@never_cache
@login_required
def tutor_crear(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.doctor_fk = doctor
            tutor.save()
            return redirect('tutor_lista')
    else:
        form = TutorForm()
    return render(request, 'tutor/form.html', {'form': form})

@never_cache
@login_required
def tutor_editar(request, pk):
    doctor = request.user.doctor
    tutor = get_object_or_404(Tutor, pk=pk, doctor_fk=doctor)
    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor_lista')
    else:
        form = TutorForm(instance=tutor)
    return render(request, 'tutor/form.html', {'form': form})

@never_cache
@login_required
def tutor_eliminar(request, pk):
    doctor = request.user.doctor
    tutor = get_object_or_404(Tutor, pk=pk, doctor_fk=doctor)
    if request.method == 'POST':
        tutor.delete()
        return redirect('tutor_lista')
    return render(request, 'tutor/confirmar_eliminar.html', {'tutor': tutor})







############
#PACIENTE

@never_cache
@login_required
def agenda(request):
    return render(request, 'agenda/index.html')

@never_cache
@login_required
def agenda_lista(request):
    doctor = request.user.doctor
    citas = Agenda.objects.filter(id_paciente_fk__doctor_fk=doctor).select_related('id_paciente_fk').order_by('fecha_hora')
    return render(request, 'agenda/lista.html', {'citas': citas})

@never_cache
@login_required
def agenda_crear(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = AgendaForm(request.POST, doctor=doctor)
        if form.is_valid():
            form.save()
            return redirect('agenda_lista')
    else:
        form = AgendaForm(doctor=doctor)
    return render(request, 'agenda/form.html', {'form': form})

@never_cache
@login_required
def agenda_editar(request, pk):
    doctor = request.user.doctor
    cita = get_object_or_404(Agenda, pk=pk, id_paciente_fk__doctor_fk=doctor)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=cita, doctor=doctor)
        if form.is_valid():
            form.save()
            return redirect('agenda_lista')
    else:
        form = AgendaForm(instance=cita, doctor=doctor)
    return render(request, 'agenda/form.html', {'form': form})

@never_cache
@login_required
def agenda_eliminar(request, pk):
    doctor = request.user.doctor
    cita = get_object_or_404(Agenda, pk=pk, id_paciente_fk__doctor_fk=doctor)
    if request.method == 'POST':
        cita.delete()
        return redirect('agenda_lista')
    return render(request, 'agenda/confirmar_eliminar.html', {'cita': cita})



############
# INVENTARIO

@never_cache
@login_required
def inventario(request):
    return render(request, 'inventario/index.html')

@never_cache
@login_required
def inventario_lista(request):
    doctor = request.user.doctor
    items = (Inventario.objects.filter(doctor_fk=doctor)
             .select_related('instrumento_fk')
             .order_by('instrumento_fk__nombre'))
    return render(request, 'inventario/lista.html', {'items': items})

@never_cache
@login_required
def inventario_editar(request, pk):
    doctor = request.user.doctor
    item = get_object_or_404(Inventario, pk=pk, doctor_fk=doctor)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventario_lista')
    else:
        form = InventarioForm(instance=item)
    return render(request, 'inventario/form.html', {'form': form, 'item': item})





############
# FICHA MÉDICA


@never_cache
@login_required
def ficha(request):
    return render(request, 'ficha/index.html')

@never_cache
@login_required
def ficha_lista(request):
    doctor = request.user.doctor
    fichas = (FichaMedica.objects.filter(id_paciente_fk__doctor_fk=doctor)
              .select_related('id_paciente_fk')
              .order_by('-id'))
    return render(request, 'ficha/lista.html', {'fichas': fichas})

@never_cache
@login_required
def ficha_crear(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = FichaMedicaForm(request.POST, doctor=doctor)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.save()
            return redirect('ficha_lista')
    else:
        form = FichaMedicaForm(doctor=doctor)
    return render(request, 'ficha/form.html', {'form': form})

@never_cache
@login_required
def ficha_editar(request, pk):
    doctor = request.user.doctor
    ficha = get_object_or_404(FichaMedica, pk=pk, id_paciente_fk__doctor_fk=doctor)
    if request.method == 'POST':
        form = FichaMedicaForm(request.POST, instance=ficha, doctor=doctor)
        if form.is_valid():
            form.save()
            return redirect('ficha_lista')
    else:
        form = FichaMedicaForm(instance=ficha, doctor=doctor)
    return render(request, 'ficha/form.html', {'form': form})

@never_cache
@login_required
def ficha_eliminar(request, pk):
    doctor = request.user.doctor
    ficha = get_object_or_404(FichaMedica, pk=pk, id_paciente_fk__doctor_fk=doctor)
    if request.method == 'POST':
        ficha.delete()
        return redirect('ficha_lista')
    return render(request, 'ficha/confirmar_eliminar.html', {'ficha': ficha})






############
# RECETA


@never_cache
@login_required
def receta(request):
    return render(request, 'receta/index.html')

@never_cache
@login_required
def receta_lista(request):
    doctor = request.user.doctor
    recetas = (Receta.objects.filter(paciente_fk__doctor_fk=doctor)
               .select_related('paciente_fk', 'medicamento_fk')
               .order_by('paciente_fk__nombre'))
    return render(request, 'receta/lista.html', {'recetas': recetas})

@never_cache
@login_required
def receta_crear(request):
    doctor = request.user.doctor
    if request.method == 'POST':
        form = RecetaForm(request.POST, doctor=doctor)
        if form.is_valid():
            form.save()
            return redirect('receta_lista')
    else:
        form = RecetaForm(doctor=doctor)
    return render(request, 'receta/form.html', {'form': form})

@never_cache
@login_required
def receta_editar(request, pk):
    doctor = request.user.doctor
    receta = get_object_or_404(Receta, pk=pk, paciente_fk__doctor_fk=doctor)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta, doctor=doctor)
        if form.is_valid():
            form.save()
            return redirect('receta_lista')
    else:
        form = RecetaForm(instance=receta, doctor=doctor)
    return render(request, 'receta/form.html', {'form': form})

@never_cache
@login_required
def receta_eliminar(request, pk):
    doctor = request.user.doctor
    receta = get_object_or_404(Receta, pk=pk, paciente_fk__doctor_fk=doctor)
    if request.method == 'POST':
        receta.delete()
        return redirect('receta_lista')
    return render(request, 'receta/confirmar_eliminar.html', {'receta': receta})
