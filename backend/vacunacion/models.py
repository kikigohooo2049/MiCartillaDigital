from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_usuario
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    CURP = models.CharField(max_length=20, unique=True)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

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
    dosis_aplicadas = models.IntegerField()
    lote = models.CharField(max_length=50)
    dosis_requeridas = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class RegistroVacunacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    centro_salud = models.ForeignKey(CentroSalud, on_delete=models.CASCADE)
    fecha_vacunacion = models.DateField()

    def __str__(self):
        return f"{self.paciente} - {self.vacuna} - {self.fecha_vacunacion}"