from rest_framework.permissions import BasePermission

class IsPersonalSalud(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol in ['medico', 'enfermera', 'sanitario', 'admin']

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'admin'