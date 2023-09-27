from django.contrib import admin
from .models import *
# Register your models here.


class DeclaracionesAdmin(admin.ModelAdmin):
    list_display = ['id', 'mision', 'vision', 'proposito', 'valores']

class EquiposAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre','fotografia_equipo','descripcion']

class PersonasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'cargo', 'equipo', 'resegna', 'fotografia_persona']

class IdeasAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha', 'hora', 'texto']


admin.site.register(Declaraciones, DeclaracionesAdmin)
admin.site.register(Equipos ,EquiposAdmin)
admin.site.register(Personas ,PersonasAdmin)
admin.site.register(Idea, IdeasAdmin)

