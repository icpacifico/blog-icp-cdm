from django.contrib import admin
from .models import *

# Register your models here.

class PracticaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_practica','is_active_centro_costo']


class Img_PracticaAdmin(admin.ModelAdmin):
    list_display = ['id','titulo_imagen','fecha_imagen','img_practica','practica','is_active_img']

admin.site.register(Practica, PracticaAdmin)
admin.site.register(Img_Practica, Img_PracticaAdmin)