from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin

from rh.models import Empleado

class Seguimiento(models.Model,PermissionRequiredMixin):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    registro = models.DateTimeField('Registro', null=True, blank=True)
    longitud = models.DecimalField('Longitud', max_digits=10, decimal_places=7, null=True, blank=True)
    latitud = models.DecimalField('Latitud', max_digits=10, decimal_places=7, null=True, blank=True)
    fecha_alta = models.DateField('Alta', auto_now_add=True)
    fecha_modificacion = models.DateField('Modificación', auto_now=True)

    class Meta:
        verbose_name = 'Ubicación' 
        verbose_name_plural = 'Ubicaciones' 
        ordering = ['empleado','-registro']
        db_table = 'Seguimiento'

    def __str__(self):
        return '%s, %s, %s-%s' % (self.empleado, self.registro, self.latitud, self.longitud)
