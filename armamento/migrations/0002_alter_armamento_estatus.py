# Generated by Django 4.0.4 on 2024-04-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamento',
            name='estatus',
            field=models.IntegerField(choices=[(0, 'Asignado'), (1, 'Baja'), (2, 'Sin Asignar'), (3, 'Taller'), (99, 'Otro')], default=1),
        ),
    ]
