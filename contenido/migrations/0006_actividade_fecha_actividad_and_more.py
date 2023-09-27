# Generated by Django 4.2.4 on 2023-09-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0005_video_img_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividade',
            name='fecha_actividad',
            field=models.DateField(null=True, verbose_name='Fecha Actividad'),
        ),
        migrations.AddField(
            model_name='actividade',
            name='portada_actividad',
            field=models.ImageField(null=True, upload_to='actividades/portadas', verbose_name='Portada'),
        ),
    ]
