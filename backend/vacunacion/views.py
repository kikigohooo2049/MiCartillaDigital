from rest_framework import viewsets
from .models import CentroSalud, Paciente, RegistroVacunacion, Usuario, Vacuna, Lote, Stock
from .serializers import (
    CentroSaludSerializer, 
    PacienteSerializer, 
    RegistroVacunacionSerializer, 
    UsuarioSerializer, 
    VacunaSerializer,
    LoteSerializer,
    StockSerializer
)
from .permissions import IsPersonalSalud, IsAdmin

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdmin]

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsPersonalSalud]

class CentroSaludViewSet(viewsets.ModelViewSet):
    queryset = CentroSalud.objects.all()
    serializer_class = CentroSaludSerializer
    permission_classes = [IsAdmin]

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    serializer_class = VacunaSerializer
    permission_classes = [IsAdmin]

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    permission_classes = [IsAdmin]

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdmin]

class RegistroVacunacionViewSet(viewsets.ModelViewSet):
    queryset = RegistroVacunacion.objects.all()
    serializer_class = RegistroVacunacionSerializer
    permission_classes = [IsPersonalSalud]

    def perform_create(self, serializer):
        serializer.save(personal=self.request.user)