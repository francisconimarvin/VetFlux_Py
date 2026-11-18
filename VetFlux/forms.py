# forms.py
from django import forms
from .models import (
    Paciente,
    Tutor,
    Agenda,
    Inventario,
    FichaMedica,
    Receta
)

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'sexo', 'especie', 'raza', 'color', 'tutor_fk']
        labels = {
            'tutor_fk': 'Tutor',
        }

    def __init__(self, *args, doctor, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tutor_fk'].queryset = Tutor.objects.filter(doctor_fk=doctor)
        self.fields['sexo'].required = True

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['rut', 'nombre', 'email', 'telefono', 'domicilio']



class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['fecha_hora', 'notas', 'id_paciente_fk']
        labels = {
            'id_paciente_fk': 'Paciente',
        }
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, doctor, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_paciente_fk'].queryset = Paciente.objects.filter(doctor_fk=doctor)




class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['cantidad']




class FichaMedicaForm(forms.ModelForm):
    class Meta:
        model = FichaMedica
        fields = ['titulo', 'descripcion', 'id_paciente_fk']
        labels = {
            'id_paciente_fk': 'Paciente',
        }

    def __init__(self, *args, doctor, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_paciente_fk'].queryset = Paciente.objects.filter(doctor_fk=doctor)



class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['paciente_fk', 'medicamento_fk', 'dosis']
        labels = {
            'paciente_fk': 'Paciente',
            'medicamento_fk': 'Medicamento',
        }

    def __init__(self, *args, doctor, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente_fk'].queryset = Paciente.objects.filter(doctor_fk=doctor)