from django.db import models

# Create your models here.
is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

class Noticia(models.Model):
    titulo_Noticia = models.CharField(verbose_name="Titulo Noticia", max_length=100, blank=False,null=False)
    fecha_noticia = models.DateField(verbose_name="Fecha Noticia")
    img_noticia = models.ImageField(verbose_name="Imagen Noticia", upload_to='noticias')
    url_noticia = models.TextField(verbose_name="Url de la Noticia")
    is_active_noticia = models.CharField(verbose_name="Estado Noticia", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                     default=is_active)
    def __str__(self):
        return self.titulo_Noticia

    class Meta:
        db_table = "noticia"