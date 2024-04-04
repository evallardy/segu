# Generated by Django 4.0.4 on 2024-04-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[(0, 'Pistola'), (1, 'Revólver'), (2, 'Fusil de asalto'), (3, 'Rifle de francotirador'), (4, 'Escopeta'), (5, 'Ametralladora ligera'), (6, 'Ametralladora pesada'), (7, 'Lanzagranadas'), (8, 'Granada'), (9, 'Otro')], default=1, max_length=10)),
                ('otro_tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('marca', models.CharField(choices=[(0, 'Smith & Wesson'), (1, 'Glock'), (2, 'Colt'), (3, 'Heckler & Koch (H&K)'), (4, 'Beretta'), (5, 'SIG Sauer'), (6, 'Remington'), (7, 'Ruger'), (8, 'Browning'), (9, 'FN Herstal'), (10, 'Mossberg'), (11, 'Winchester'), (12, 'Springfield Armory'), (13, 'Taurus'), (14, 'CZ (Česká zbrojovka)'), (15, 'Otro')], default=1, max_length=10)),
                ('otra_marca', models.CharField(blank=True, max_length=100, null=True)),
                ('modelo', models.CharField(blank=True, max_length=100, null=True)),
                ('calibre', models.CharField(choices=[(0, '5.56x45mm NATO (.223 Remington)'), (1, '7.62x51mm NATO (.308 Winchester)'), (2, '9mm Parabellum (9x19mm)'), (3, '.45 ACP (11.43x23mm)'), (4, '.380 ACP (9x17mm)'), (5, '.357 Magnum (9x33mmR)'), (6, '.44 Magnum (10.9x33mmR)'), (7, '.38 Special (9x29mmR)'), (8, '12 Gauge (Calibre 12)'), (9, '20 Gauge (Calibre 20)'), (10, 'Otro')], default=1, max_length=50)),
                ('otro_calibre', models.CharField(blank=True, max_length=100, null=True)),
                ('capacidad_cargador', models.IntegerField()),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('estatus', models.CharField(choices=[(0, 'Baja'), (1, 'Sin Asignar'), (2, 'Asignado'), (3, 'Taller'), (4, 'Otro')], max_length=100)),
            ],
            options={
                'verbose_name': 'Armamento',
                'verbose_name_plural': 'Armas',
                'db_table': 'Armamento',
                'ordering': ['numero_serie'],
            },
        ),
    ]
