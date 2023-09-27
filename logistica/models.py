from django.db import models

# Create your models here.
is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

class Reporte(models.Model):
    titulo_reporte = models.CharField(verbose_name="Titulo Reporte", max_length=100, blank=False,null=False)
    fecha_reporte = models.DateField(verbose_name="Fecha Reporte")
    url_reporte = models.TextField(verbose_name="Url de la Reporte")
    is_active_reporte = models.CharField(verbose_name="Estado Reporte", max_length=10, blank=False, null=False,
                                         choices=IS_ACTIVE_CHOICES,
                                         default=is_active)
    def __str__(self):
        return self.titulo_reporte

    class Meta:
        db_table = "reporte"