from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    UsuarioViewSet,
    PacienteViewSet,
    CentroSaludViewSet,
    VacunaViewSet,
    RegistroVacunacionViewSet,
    LoteViewSet,
    StockViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'centros-salud', CentroSaludViewSet)
router.register(r'vacunas', VacunaViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'stock', StockViewSet)
router.register(r'registros', RegistroVacunacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]