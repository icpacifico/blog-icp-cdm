# Generated by Django 4.2.4 on 2023-09-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sustentabilidad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img_practica',
            name='imagen',
        ),
    ]
