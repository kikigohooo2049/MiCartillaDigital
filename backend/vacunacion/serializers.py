from rest_framework import serializers
from .models import CentroSalud, Paciente, RegistroVacunacion, Usuario, Vacuna, Lote, Stock

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nombre', 'apellido', 'fecha_nacimiento', 'CURP', 'domicilio', 'telefono', 'sexo', 'edad']

class CentroSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroSalud
        fields = ['id', 'nombre', 'direccion', 'telefono']

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['id', 'nombre', 'dosis_requeridas']

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lote
        fields = ['id', 'vacuna', 'codigo', 'fecha_caducidad']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'centro_salud', 'lote', 'cantidad']

class RegistroVacunacionSerializer(serializers.ModelSerializer):
    personal = serializers.ReadOnlyField(source='personal.id')

    class Meta:
        model = RegistroVacunacion
        fields = ['id', 'paciente', 'vacuna', 'lote', 'centro_salud', 'personal', 'fecha_vacunacion']