from django.db import models

# Create your models here.
is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

class Practica(models.Model):
    nombre_practica = models.CharField(verbose_name="Titulo", max_length=80, blank=False,null=False)
    descripcion = models.TextField()
    is_active_centro_costo = models.CharField(verbose_name="Estado Practica", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                              default=is_active)

    def __str__(self):
        return self.nombre_practica

    class Meta:
        db_table = "practica_sus"


class Img_Practica(models.Model):
    titulo_imagen = models.CharField(verbose_name="Titulo Imagen", max_length=50, blank=False,null=False)
    fecha_imagen = models.DateField(verbose_name="Fecha Imagen")
    img_practica = models.ImageField(verbose_name="Imagen", upload_to='sustentabilidad')
    practica = models.ForeignKey(Practica,verbose_name="Practica Asociada",  on_delete=models.CASCADE)
    is_active_img = models.CharField(verbose_name="Esatdo Imagen", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                              default=is_active)

    def __str__(self):
        return self.titulo_imagen

    class Meta:
        db_table = "img_prac_sustentable"
