from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('medico', 'Médico'),
        ('enfermera', 'Enfermera'),
        ('sanitario', 'Sanitario'),
    )
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='sanitario')

    def __str__(self):
        return self.username

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    CURP = models.CharField(max_length=20, unique=True)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class CentroSalud(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    dosis_requeridas = models.IntegerField()

    def __str__(self):
        return self.nombre

class Lote(models.Model):
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    fecha_caducidad = models.DateField()

    def __str__(self):
        return f"{self.vacuna.nombre} - {self.codigo}"

class Stock(models.Model):
    centro_salud = models.ForeignKey(CentroSalud, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.centro_salud.nombre} - {self.lote.codigo}"

class RegistroVacunacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    centro_salud = models.ForeignKey(CentroSalud, on_delete=models.CASCADE)
    personal = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_vacunacion = models.DateField()

    def __str__(self):
        return f"{self.paciente} - {self.vacuna} - {self.fecha_vacunacion}"