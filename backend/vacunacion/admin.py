from django.contrib import admin

# Register your models here.

from .models import Usuario, Paciente, CentroSalud, Vacuna, RegistroVacunacion
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(CentroSalud)
admin.site.register(Vacuna)
admin.site.register(RegistroVacunacion)

