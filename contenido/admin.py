from django.contrib import admin
from .models import *


# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo_video', 'fecha_video', 'url_video', 'is_active_video']


class HitoAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria_hito', 'titulo_hit', 'fecha_hito', 'lugar_hito', 'is_active_hito']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo_banner', 'fecha_banner', 'foto_banner', 'is_active_banner']


class Img_ActividadeInline(admin.TabularInline):
    model = Img_Actividade
    extra = 4


class Img_ActividadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo_imagen', 'fecha_imagen', 'img_actividad', 'actividad', 'is_active_img']


class ActividadAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria_actividad', 'nombre_actividad', 'fecha_actividad', 'portada_actividad', 'is_active_actividad']
    inlines = [Img_ActividadeInline, ]


class InformativoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_informativo', 'portada_informativo', 'fecha_informativo', 'is_active_informativo']


class IndicadoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo_kpis', 'fecha_kpis', 'url_kpis', 'is_active_kpis']


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'autor', 'texto', 'fecha']


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'autor', 'texto', 'fecha']


admin.site.register(Video, VideoAdmin)
admin.site.register(Hito, HitoAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Actividade, ActividadAdmin)
admin.site.register(Img_Actividade, Img_ActividadeAdmin)
admin.site.register(Informativo, InformativoAdmin)
admin.site.register(Indicadore, IndicadoresAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
