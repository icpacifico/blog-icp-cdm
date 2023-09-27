from django.db import models
from blogapp.models import *
# Create your models here.


is_active = 'Activo'
is_inactive = 'Inactivo'

IS_ACTIVE_CHOICES = [(is_active, 'Activo'),
                     (is_inactive, 'Inactivo'), ]

cumple = 'Cumpleaños'
event = 'Evento'
taller = 'Taller'
premio = 'Premiación'

CAT_ACT_CHOISES = [(cumple, 'Cumpleaños'),
                     (event, 'Evento'),
                     (taller, 'Taller'),
                     (premio, 'Premiación'),]

show = 'Mostrar'
hide = 'Ocultar'

SHOW_CHOISES = [(show, 'Mostrar'),
                     (hide, 'Ocultar'), ]

actual = 'Actual'
proximos = 'Próximo'

HITO_CHOISES = [(actual, 'Actual'),
                     (proximos, 'Próximo'), ]


class Video(models.Model):
    titulo_video = models.CharField(verbose_name="Titulo Video", max_length=50, blank=False,null=False)
    fecha_video = models.DateField(verbose_name="Fecha del Video")
    url_video = models.TextField(verbose_name="Url del Video")
    img_video = models.ImageField(verbose_name="Foto", upload_to="videos", null=True)
    is_active_video = models.CharField(verbose_name="Estado Video", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                     default=is_active)

    def __str__(self):
        return self.titulo_video

    class Meta:
        db_table = "video"



class Hito(models.Model):
    categoria_hito = models.CharField(verbose_name="Categoria Hito", max_length=10, blank=False, null=False,
                                           choices=HITO_CHOISES,
                                           default=actual)
    titulo_hit = models.CharField(verbose_name="Titulo Hito", max_length=50, blank=False,null=False)
    fecha_hito = models.DateField(verbose_name="Fecha")
    lugar_hito = models.CharField(verbose_name="Lugar Hito", max_length=50, blank=False,null=False)
    img_hito = models.ImageField(verbose_name="Foto", upload_to="hitos", null=True)
    is_active_hito = models.CharField(verbose_name="Estado Hito", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                     default=is_active)

    def __str__(self):
        return self.titulo_hit

    class Meta:
        db_table = "hito"


class Actividade(models.Model):
    categoria_actividad = models.CharField(verbose_name="Categoria Actividad", max_length=10, blank=False, null=False, choices=CAT_ACT_CHOISES,
                                              default=event)
    nombre_actividad = models.CharField(verbose_name="Actividad", max_length=80, blank=False,null=False)
    portada_actividad = models.ImageField(verbose_name="Portada", upload_to='actividades/portadas', null=True)
    fecha_actividad = models.DateField(verbose_name="Fecha Actividad", null=True)
    resegna_actividad = models.TextField(verbose_name="Reseña de la Actividad")
    mostrar_inicio = models.CharField(verbose_name="Mostrar en Inicio", max_length=10, blank=False, null=False, choices=SHOW_CHOISES,
                                              default=hide)
    is_active_actividad = models.CharField(verbose_name="Estado Actividad", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                              default=is_active)

    def __str__(self):
        return self.nombre_actividad

    class Meta:
        db_table = "actividad"


class Img_Actividade(models.Model):
    titulo_imagen = models.TextField(verbose_name="Titulo Imagen", blank=False,null=False)
    fecha_imagen = models.DateField(verbose_name="Fecha Imagen")
    img_actividad = models.ImageField(verbose_name="Imagen", upload_to='actividades')
    actividad = models.ForeignKey(Actividade,verbose_name="Actividad Asociada",  on_delete=models.CASCADE)
    is_active_img = models.CharField(verbose_name="Esatdo Imagen", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                              default=is_active)

    def __str__(self):
        return self.titulo_imagen

    class Meta:
        db_table = "img_actividad"


class Banner(models.Model):
    actividad_banner = models.ForeignKey(Actividade, verbose_name="Actividad Asociada" , on_delete=models.CASCADE)
    titulo_banner = models.CharField(verbose_name="Titulo Banner", max_length=50, blank=False,null=False)
    resegna_banner = models.TextField(verbose_name="Reseña del Banner")
    fecha_banner = models.DateField(verbose_name="Fecha Foto")
    foto_banner = models.ImageField(verbose_name="Foto", upload_to='banners')
    is_active_banner = models.CharField(verbose_name="Estado banner", max_length=10, blank=False, null=False, choices=IS_ACTIVE_CHOICES,
                                     default=is_active)

    def __str__(self):
        return self.titulo_banner

    class Meta:
        db_table = "banner"


class Informativo(models.Model):
    nombre_informativo = models.CharField(verbose_name="Informativo", max_length=80, blank=False, null=False)
    nombre_responsable = models.ForeignKey(Personas, verbose_name="Responsable", on_delete=models.CASCADE, null=True)
    area_informativo = models.ForeignKey(Equipos, verbose_name="Área", on_delete=models.CASCADE, null=True)
    portada_informativo = models.ImageField(verbose_name="Portada", upload_to='informativos', null=True)
    fecha_informativo = models.DateField(verbose_name="Fecha informativo", null=True)
    is_active_informativo = models.CharField(verbose_name="Estado Informativo", max_length=10, blank=False, null=False,
                                           choices=IS_ACTIVE_CHOICES,
                                           default=is_active)

    def __str__(self):
        return self.nombre_informativo

    class Meta:
        db_table = "informativo"


class Indicadore(models.Model):
    titulo_kpis = models.CharField(verbose_name="Titulo Kpi", max_length=100, blank=False,null=False)
    fecha_kpis = models.DateField(verbose_name="Fecha Reporte")
    url_kpis = models.TextField(verbose_name="Url del Reporte")
    is_active_kpis = models.CharField(verbose_name="Estado Reporte", max_length=10, blank=False, null=False,
                                         choices=IS_ACTIVE_CHOICES,
                                         default=is_active)
    def __str__(self):
        return self.titulo_kpis

    class Meta:
        db_table = "indicadores"

class Comentario(models.Model):
    post = models.ForeignKey(Actividade, on_delete=models.CASCADE, related_name='comentarios')
    #autor = models.ForeignKey(User,on_delete=models.CASCADE)  # Si deseas que los comentarios estén vinculados a usuarios registrados
    autor = models.CharField(max_length=30,verbose_name="Autor")
    texto = models.TextField(verbose_name="Cometario")
    fecha = models.DateTimeField(verbose_name="Fecha", auto_now_add=True)

    # Puedes agregar otros campos según tus necesidades, como un campo para respuestas


class Respuesta(models.Model):
    comment = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respuestas')
    #autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Si deseas que las respuestas estén vinculadas a usuarios registrados
    autor = models.CharField(max_length=30,verbose_name="Autor")
    texto = models.TextField(verbose_name="Respuesta")
    fecha = models.DateTimeField(verbose_name="Fecha", auto_now_add=True)