# Generated by Django 4.2.4 on 2023-09-01 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_practica', models.CharField(max_length=80, verbose_name='Titulo')),
                ('is_active_centro_costo', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
            options={
                'db_table': 'practica_sus',
            },
        ),
        migrations.CreateModel(
            name='Img_Practica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('titulo_imagen', models.CharField(max_length=50, verbose_name='Titulo Imagen')),
                ('fecha_imagen', models.DateField()),
                ('img_practica', models.ImageField(upload_to='sustentabilidad')),
                ('is_active_img', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('practica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sustentabilidad.practica')),
            ],
            options={
                'db_table': 'img_prac_sustentable',
            },
        ),
    ]
