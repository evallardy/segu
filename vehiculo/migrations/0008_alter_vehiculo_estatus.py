# Generated by Django 4.0.4 on 2024-04-01 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0007_alter_vehiculo_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='estatus',
            field=models.CharField(max_length=2, verbose_name='Estatus'),
        ),
    ]