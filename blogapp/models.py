from django.db import models

# Create your models here.

class Declaraciones(models.Model):
    mision = models.TextField(verbose_name="Misión")
    vision = models.TextField(verbose_name="Visión")
    proposito = models.TextField(verbose_name="Propósito")
    valores = models.TextField(verbose_name="Valores")

    class Meta:
        db_table = "declaraciones"

class Equipos(models.Model):
    nombre = models.CharField(verbose_name="Nombre Equipo", max_length=100, blank=False, null=False)
    fotografia_equipo = models.ImageField(verbose_name="Foto Equipo", upload_to='equipos')
    descripcion = models.TextField(verbose_name="Descripción Equipo")
    frase = models.TextField(verbose_name='Frase del Equipo')
    per_frase = models.TextField(verbose_name='Persona')
    cargo_per = models.TextField(verbose_name='Cargo')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "equipos"


class Personas(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100, blank=False, null=False)
    apellido = models.CharField(verbose_name="Apellido", max_length=100, blank=False, null=False)
    cargo = models.CharField(verbose_name="Cargo", max_length=100, blank=False, null=False)
    equipo = models.ForeignKey(Equipos,verbose_name="Equipo Asociado",  on_delete=models.CASCADE)
    resegna = models.TextField(verbose_name="Reseña")
    fotografia_persona = models.ImageField(verbose_name="Foto", upload_to='personas')
    correo = models.EmailField()
    telefono = models.CharField(verbose_name="Teléfono", max_length=12, blank=False, null=False)
    def __str__(self):
        return self.nombre + " " +self.apellido


    class Meta:
        db_table = "personas"

class Idea(models.Model):
    texto = models.TextField(verbose_name="Texto")
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)

    def __str__(self):
        return self.id


    class Meta:
        db_table = "ideas"