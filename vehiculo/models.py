from django.db import models

from core.contantes import TIPO_COMBUSTIBLE, MARCA_VEHICULO, TIPO_VEHICULO, ESTATUS_VEHICULO

class Vehiculo(models.Model):
    marca = models.IntegerField('Marca', choices=MARCA_VEHICULO,default=1)
    otra_marca = models.CharField('Otra marca', max_length=100, blank=True, null=True)
    modelo = models.CharField('Modelo', max_length=100, blank=True, null=True)
    anio = models.IntegerField('Año')
    placa = models.CharField('Placa', max_length=10, unique=True, blank=True, null=True)
    color = models.CharField('Color', max_length=50)
    tipo_combustible = models.IntegerField('Combustible', choices=TIPO_COMBUSTIBLE, default=1)
    otro_tipo_combustible = models.CharField('Otro combustible', max_length=50, blank=True, null=True)
    tipo_vehiculo = models.IntegerField('Tipo vehículo', choices=TIPO_VEHICULO, default=1)
    otro_tipo_vehiculo = models.CharField('Otro tipo de Vehículo', max_length=100, blank=True, null=True)
    numero_serie = models.CharField('Número serie', max_length=50)
    fecha_alta = models.DateField('Alta')
    fecha_baja = models.DateField('Baja', blank=True, null=True)
    estatus = models.IntegerField('Estatus', choices=ESTATUS_VEHICULO, default=1)

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering = ['placa']
        db_table = 'Vehiculo'

    def __str__(self):
        return '%s %s %s %s' % (self.tipo, self.marca, self.modelo, self.placa)


