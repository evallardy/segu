# Generated by Django 4.0.4 on 2024-04-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0013_alter_vehiculo_numero_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.IntegerField(choices=[(1, 'Audi'), (2, 'BMW'), (3, 'Chevrolet'), (4, 'Ford'), (5, 'Honda'), (6, 'Hyundai'), (7, 'Kia'), (8, 'Lexus'), (9, 'Mazda'), (10, 'Mercedes-Benz'), (11, 'Nissan'), (12, 'Subaru'), (13, 'Tesla'), (14, 'Toyota'), (15, 'Volkswagen'), (99, 'Otra')], default=1, verbose_name='Marca'),
        ),
    ]