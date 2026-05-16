from rest_framework import viewsets

# Importamos todos nuestros modelos
from .models import CentroSalud, Paciente, RegistroVacunacion, Usuario, Vacuna

# Importamos todos los traductores (serializers) que acabas de crear
from .serializers import (
    CentroSaludSerializer, 
    PacienteSerializer, 
    RegistroVacunacionSerializer, 
    UsuarioSerializer, 
    VacunaSerializer
)

# Creamos un viewset para cada modelo
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class CentroSaludViewSet(viewsets.ModelViewSet):
    queryset = CentroSalud.objects.all()
    serializer_class = CentroSaludSerializer

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer

class RegistroVacunacionViewSet(viewsets.ModelViewSet):
    queryset = RegistroVacunacion.objects.all()
    serializer_class = RegistroVacunacionSerializer

