# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings

class Agenda(models.Model):
    fecha_hora = models.DateTimeField()
    notas = models.TextField(blank=True, null=True)
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk')

    class Meta:
        managed = False
        db_table = 'agenda'

    def __str__(self):
        return f"{self.fecha_hora:%d/%m/%Y %H:%M} - {self.id_paciente_fk.nombre}"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

    def __str__(self):
        return self.name


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

    def __str__(self):
        return self.name


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

    def __str__(self):
        return f"{self.app_label} | {self.model}"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

    def __str__(self):
        return self.session_key


class Doctor(models.Model):
    rut = models.CharField(primary_key=True, max_length=16)
    nombre = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150)
    telefono = models.CharField(unique=True, max_length=10)
    activo = models.BooleanField()
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, models.DO_NOTHING,
                                   blank=True, null=True, db_column='usuario_id')

    class Meta:
        managed = False
        db_table = 'doctor'

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class FichaMedica(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk')

    class Meta:
        managed = False
        db_table = 'ficha_medica'

    def __str__(self):
        return f"{self.titulo} - {self.id_paciente_fk.nombre}"


class Instrumentos(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrumentos'

    def __str__(self):
        return self.nombre or f"Instrumento {self.pk}"


class Inventario(models.Model):
    cantidad = models.IntegerField()
    instrumento_fk = models.ForeignKey(Instrumentos, models.DO_NOTHING, db_column='instrumento_fk')
    doctor_fk = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_fk')

    class Meta:
        managed = False
        db_table = 'inventario'
        unique_together = (('instrumento_fk', 'doctor_fk'),)

    def __str__(self):
        return f"{self.instrumento_fk} ({self.cantidad})"


class Medicamentos(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'medicamentos'

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True,
                            choices=[('H', 'Hembra'), ('M', 'Macho')])
    especie = models.CharField(max_length=20,
                           choices=[('Canino', 'Canino'), ('Felino', 'Felino')])
    raza = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    tutor_fk = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='tutor_fk', blank=True, null=True)
    doctor_fk = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_fk')

    class Meta:
        managed = False
        db_table = 'paciente'

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Receta(models.Model):
    dosis = models.CharField(max_length=50)
    paciente_fk = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_fk')
    medicamento_fk = models.ForeignKey(Medicamentos, models.DO_NOTHING, db_column='medicamento_fk')

    class Meta:
        managed = False
        db_table = 'receta'

    def __str__(self):
        return f"{self.medicamento_fk} - {self.paciente_fk.nombre} ({self.dosis})"


class Tutor(models.Model):
    rut = models.CharField(primary_key=True, max_length=16)
    nombre = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150)
    telefono = models.CharField(unique=True, max_length=11)
    domicilio = models.CharField(max_length=200, blank=True, null=True)
    doctor_fk = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_fk')

    class Meta:
        managed = False
        db_table = 'tutor'

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
