from django.contrib import admin
from .models import *
# Register your models here.


class PlanificacionAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'titulo_planificacion',
                    'fecha_planificacion',
                    'url_planificacion',
                    'is_active_planificacion']


admin.site.register(Planificacione, PlanificacionAdmin)

