#Usamos DefaultRouter para generar automáticamente las rutas de la API

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    PacienteViewSet,
    CentroSaludViewSet,
    VacunaViewSet,
    RegistroVacunacionViewSet
)

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'centros-salud', CentroSaludViewSet)
router.register(r'vacunas', VacunaViewSet)
router.register(r'registros', RegistroVacunacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]