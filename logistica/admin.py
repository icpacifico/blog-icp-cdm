from django.contrib import admin
from .models import *
# Register your models here.


class ReporteAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'titulo_reporte',
                    'fecha_reporte',
                    'url_reporte',
                    'is_active_reporte']


admin.site.register(Reporte, ReporteAdmin)
