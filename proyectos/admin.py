from django.contrib import admin
from .models import *

# Register your models here.


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_proyecto','descripcion_proyecto']


class Img_ProyectoAdmin(admin.ModelAdmin):
    list_display = ['id','titulo_imagen','fecha_imagen','img_proyecto','proyecto','is_active_img']

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Img_Proyecto, Img_ProyectoAdmin)