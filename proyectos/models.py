from django.db import models

# Create your models here.
is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(verbose_name="Nombre Proyecto", max_length=30, blank=False,null=False)
    descripcion_proyecto = models.TextField(verbose_name="Descripción del Proyecto")

    def __str__(self):
        return self.nombre_proyecto

    class Meta:
        db_table = "proyectos"


class Img_Proyecto(models.Model):
    titulo_imagen = models.CharField(verbose_name="Titulo Imagen", max_length=50, blank=False,null=False)
    fecha_imagen = models.DateField(verbose_name="Fecha de la Imagen")
    img_proyecto = models.ImageField(verbose_name="Imagen del proyecto", upload_to='proyectos')
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto asociado", on_delete=models.CASCADE)
    is_active_img = models.CharField(verbose_name="Estado Imagen", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                              default=is_active)

    def __str__(self):
        return self.titulo_imagen

    class Meta:
        db_table = "img_proyectos"
