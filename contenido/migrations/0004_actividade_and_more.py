# Generated by Django 4.2.4 on 2023-09-04 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_alter_banner_fecha_banner_alter_banner_foto_banner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actividad', models.CharField(max_length=80, verbose_name='Actividad')),
                ('is_active_actividad', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado Actividad')),
            ],
            options={
                'db_table': 'actividad',
            },
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='is_active_video',
            new_name='is_active_banner',
        ),
        migrations.RenameField(
            model_name='cumpleagno',
            old_name='is_active_video',
            new_name='is_active_cumple',
        ),
        migrations.CreateModel(
            name='Img_Actividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_imagen', models.CharField(max_length=50, verbose_name='Titulo Imagen')),
                ('fecha_imagen', models.DateField(verbose_name='Fecha Imagen')),
                ('img_actividad', models.ImageField(upload_to='actividades', verbose_name='Imagen')),
                ('is_active_img', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Esatdo Imagen')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.actividade', verbose_name='Actividad Asociada')),
            ],
            options={
                'db_table': 'img_actividad',
            },
        ),
    ]
