from django.contrib import admin
from .models import *
# Register your models here.


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo_Noticia', 'fecha_noticia', 'img_noticia', 'url_noticia', 'is_active_noticia']


admin.site.register(Noticia, NoticiaAdmin)
