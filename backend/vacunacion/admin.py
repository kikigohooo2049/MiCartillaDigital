from django.contrib import admin
from .models import Usuario, Paciente, CentroSalud, Vacuna, RegistroVacunacion, Lote, Stock

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(CentroSalud)
admin.site.register(Vacuna)
admin.site.register(Lote)
admin.site.register(Stock)
admin.site.register(RegistroVacunacion)