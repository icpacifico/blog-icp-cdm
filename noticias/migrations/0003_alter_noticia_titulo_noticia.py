# Generated by Django 4.2.4 on 2023-09-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_alter_noticia_fecha_noticia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo_Noticia',
            field=models.CharField(max_length=100, verbose_name='Titulo Noticia'),
        ),
    ]