# Generated by Django 4.0.4 on 2024-04-02 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0004_rename_otro_tipo_armamento_otro_tipo_arma_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armamento',
            old_name='fecha_registro',
            new_name='fecha_alta',
        ),
    ]