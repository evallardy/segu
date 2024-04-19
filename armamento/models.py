from django.db import models
from core.contantes import TIPO_ARMAMENTO, ESTATUS_ARMAMENTO, TIPO_CALIBRE, MARCA_ARMAMENTO

class Armamento(models.Model):
    tipo_arma = models.IntegerField(choices=TIPO_ARMAMENTO, default=1)
    otro_tipo_arma = models.CharField(max_length=100, blank=True, null=True)    
    marca = models.IntegerField(choices=MARCA_ARMAMENTO, default=1)
    otra_marca = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    calibre = models.IntegerField(choices=TIPO_CALIBRE, default=1)
    otro_calibre = models.CharField(max_length=100, blank=True, null=True)
    capacidad_cargador = models.IntegerField()
    numero_serie = models.CharField(max_length=100)
    fecha_alta = models.DateField(auto_created=True)
    fecha_baja = models.DateField(blank=True, null=True)
    estatus = models.IntegerField(choices=ESTATUS_ARMAMENTO, default=2)

    class Meta:
        verbose_name = 'Armamento'
        verbose_name_plural = 'Armas'
        ordering = ['numero_serie']
        unique_together= ('numero_serie',)
        db_table = 'Armamento'

    def __str__(self):
        return '%s %s %s' % (self.tipo, self.modelo, self.numero_serie)
