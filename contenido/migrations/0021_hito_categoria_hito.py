# Generated by Django 4.2.4 on 2023-09-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0020_comentario_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='hito',
            name='categoria_hito',
            field=models.CharField(choices=[('Actual', 'Actual'), ('Próximo', 'Próximo')], default='Actual', max_length=10, verbose_name='Categoria Hito'),
        ),
    ]
