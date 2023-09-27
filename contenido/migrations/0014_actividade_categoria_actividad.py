# Generated by Django 4.2.4 on 2023-09-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0013_indicadore'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividade',
            name='categoria_actividad',
            field=models.CharField(choices=[('Cumpleaños', 'Cumpleaños'), ('Evento', 'Evento'), ('Taller', 'Taller'), ('Premiación', 'Premiación')], default='Evento', max_length=10, verbose_name='Categoria Actividad'),
        ),
    ]