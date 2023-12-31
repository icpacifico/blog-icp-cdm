# Generated by Django 4.2.4 on 2023-08-18 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Declaraciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mision', models.TextField()),
                ('vision', models.TextField()),
                ('proposito', models.TextField()),
                ('valores', models.TextField()),
            ],
            options={
                'db_table': 'declaraciones',
            },
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fotografia_equipo', models.ImageField(upload_to='')),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'equipos',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('resegna', models.TextField()),
                ('fotografia_persona', models.ImageField(upload_to='')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.equipos')),
            ],
            options={
                'db_table': 'personas',
            },
        ),
    ]
