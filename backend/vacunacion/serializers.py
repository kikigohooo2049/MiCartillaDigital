from rest_framework import serializers
from .models import Paciente, Vacuna

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = '__all__'

class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['lote']

class CentroSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['centro_salud']
class LoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['lote']

class CentroSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacuna
        fields = ['centro_salud']

