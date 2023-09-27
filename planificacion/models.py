from django.db import models

# Create your models here.
is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

class Planificacione(models.Model):
    titulo_planificacion = models.CharField(verbose_name="Titulo Noticia", max_length=100, blank=False,null=False)
    fecha_planificacion = models.DateField(verbose_name="Fecha Planificación")
    url_planificacion = models.TextField(verbose_name="Url de la Planificación")
    is_active_planificacion = models.CharField(verbose_name="Estado Planificación", max_length=10, blank=False, null=False,
                                         choices=IS_ACTIVE_CHOICES,
                                         default=is_active)
    def __str__(self):
        return self.titulo_planificacion

    class Meta:
        db_table = "planificacion"