# Generated by Django 4.0.4 on 2024-04-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignacion', '0003_alter_asignacion_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignacion',
            name='ubicacion',
            field=models.JSONField(blank=True, null=True, verbose_name='Ubicación'),
        ),
    ]