from django.db import models

from rh.models import Empleado
from vehiculo.models import Vehiculo
from cliente.models import Cliente

from core.contantes import ESTATUS_SERVICIO, TIPO_SERVICIO

class Asignacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    empleados = models.ManyToManyField(Empleado)
    vehiculos = models.ManyToManyField(Vehiculo)
    servicio = models.IntegerField('Servicio', choices=TIPO_SERVICIO,default=1)
    otro_servicio = models.CharField('Otro servicio', max_length=100, blank=True, null=True)
    detalle = models.TextField('Detalle', blank=True, null=True, max_length=1500)
    ubicacion = models.JSONField('Ubicación', blank=True, null=True)
    cobro = models.DecimalField('Cobro', max_digits=11, decimal_places=2, default=0)
    fecha_inicial = models.DateField('Inicia')
    fecha_termina = models.DateField('Termina', blank=True, null=True)
    fecha_alta = models.DateField('Alta', auto_now_add=True)
    fecha_baja = models.DateField('Baja', auto_now=True)
    estatus = models.IntegerField('Estatus', choices=ESTATUS_SERVICIO, default=4)

    class Meta:
        verbose_name = 'Asignación'
        verbose_name_plural = 'Asignaciones'
        ordering = ['-fecha_inicial']
        db_table = 'Asignacion'

    def __str__(self):
        return '%s %s %s' % (self.cliente, self.get_servicio_display, self.fecha_inicial)


