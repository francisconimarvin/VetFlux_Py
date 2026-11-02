# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    fecha_hora = models.DateTimeField(unique=True)
    notas = models.TextField(blank=True, null=True)
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk')

    class Meta:
        managed = False
        db_table = 'agenda'


class Doctor(models.Model):
    rut = models.CharField(primary_key=True, max_length=16)
    nombre = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150)
    telefono = models.CharField(unique=True, max_length=10)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'doctor'


class FichaMedica(models.Model):
    fecha_ficha = models.DateTimeField()
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    id_paciente_fk = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente_fk')

    class Meta:
        managed = False
        db_table = 'ficha_medica'


class Instrumentos(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instrumentos'


class Inventario(models.Model):
    cantidad = models.IntegerField()
    instrumento_fk = models.ForeignKey(Instrumentos, models.DO_NOTHING, db_column='instrumento_fk')
    doctor_fk = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_fk')

    class Meta:
        managed = False
        db_table = 'inventario'
        unique_together = (('instrumento_fk', 'doctor_fk'),)


class Medicamentos(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'medicamentos'


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    especie = models.CharField(max_length=20)
    raza = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    tutor_fk = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='tutor_fk', blank=True, null=True)
    doctor_fk = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_fk')

    class Meta:
        managed = False
        db_table = 'paciente'


class Receta(models.Model):
    dosis = models.CharField(max_length=50)
    paciente_fk = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_fk')
    medicamento_fk = models.ForeignKey(Medicamentos, models.DO_NOTHING, db_column='medicamento_fk')

    class Meta:
        managed = False
        db_table = 'receta'


class Sesiones(models.Model):
    id = models.UUIDField(primary_key=True)
    doctor_fk = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='doctor_fk')
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    revoked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sesiones'


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


class Usuarios(models.Model):
    fk_doctor = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='fk_doctor', blank=True, null=True)
    passwd = models.CharField(max_length=258)
    role = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'usuarios'
