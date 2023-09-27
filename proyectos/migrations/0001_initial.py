# Generated by Django 4.2.4 on 2023-09-01 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=30, verbose_name='Nombre Proyecto')),
                ('descripcion_proyecto', models.TextField()),
            ],
            options={
                'db_table': 'proyectos',
            },
        ),
        migrations.CreateModel(
            name='Img_Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('titulo_imagen', models.CharField(max_length=50, verbose_name='Titulo Imagen')),
                ('fecha_imagen', models.DateField()),
                ('img_proyecto', models.ImageField(upload_to='proyectos')),
                ('is_active_img', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto')),
            ],
            options={
                'db_table': 'img_proyectos',
            },
        ),
    ]
