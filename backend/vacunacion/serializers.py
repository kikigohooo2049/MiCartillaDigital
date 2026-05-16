from rest_framework import serializers
from .models import CentroSalud, Paciente, RegistroVacunacion, Usuario, Vacuna

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuario', 'email']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'apellido', 'fecha_nacimiento', 'CURP', 'domicilio', 'telefono']

class CentroSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroSalud
        fields = ['id', 'nombre', 'direccion', 'telefono']

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['id', 'nombre', 'dosis_aplicadas', 'lote', 'dosis_requeridas']

class RegistroVacunacionSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    vacuna = VacunaSerializer()
    centro_salud = CentroSaludSerializer()

    class Meta:
        model = RegistroVacunacion
        fields = ['id', 'paciente', 'vacuna', 'centro_salud', 'fecha_vacunacion']

