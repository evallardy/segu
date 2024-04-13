from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone

from core.contantes import *

class Cliente(models.Model,PermissionRequiredMixin):
    fisica_moral = models.IntegerField('Física/Moral', choices=TIPO_PERSONA, default=0)
    razon = models.CharField('Nombre', max_length=200, null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=35, null=True, blank=True)
    paterno = models.CharField('Paterno', max_length=35, null=True, blank=True)
    materno = models.CharField('Materno', max_length=35, null=True, blank=True)
    rfc = models.CharField('R.F.C.', max_length=18, null=True, blank=True)
    curp = models.CharField('CURP', max_length=18, null=True, blank=True)
    domicilio = models.JSONField('Domicilio', null=True, blank=True)
    fecha_alta = models.DateField('Alta', default=timezone.now)
    fecha_baja = models.DateField('Baja', blank=True, null=True)
    estatus = models.IntegerField('Estatus', choices=ESTATUS_BAJA_ACTIVO, default=1)

    def fecha_alta_default(self):
        return timezone.now()

    def save(self, *args, **kwargs):
        if not self.fecha_alta:
            self.fecha_alta = self.fecha_alta_default()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Cliente' 
        verbose_name_plural = 'Clientes' 
        ordering = ['fisica_moral','razon','paterno', 'materno', 'nombre']
        db_table = 'Cliente'

    def __str__(self):
#        return '%s %s %s %s %s' % (self.fisica_moral, self.razon, self.paterno, self.materno, self.nombre)
        if self.fisica_moral == 1:
            return str(self.razon)
        elif self.fisica_moral == 0:
            # Concatenar los campos paterno, materno y nombre
            nombre_completo = self.paterno
            if self.materno:
                nombre_completo += ' ' + self.materno
            nombre_completo += ' ' + self.nombre
            return nombre_completo
        else:
            # Si el valor de fisica_moral no es 0 ni 1, devuelve una cadena vacía
            return ''