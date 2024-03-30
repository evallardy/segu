from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from core.contantes import *

class Empleado(models.Model,PermissionRequiredMixin):
    codigo = models.CharField('Código', max_length=35, null=True, blank=True)
    nombre = models.CharField('Nombre', max_length=35)
    paterno = models.CharField('Paterno', max_length=35)
    materno = models.CharField('Materno', max_length=35, null=True, blank=True)
    rfc = models.CharField('R.F.C.', max_length=18, null=True, blank=True)
    curp = models.CharField('CURP', max_length=18)
    genero = models.IntegerField('Género', choices=GENERO)
    estatus = models.IntegerField('Estatus', choices=ESTATUS_BAJA_ACTIVO)

    class Meta:
        verbose_name = 'Empleado' 
        verbose_name_plural = 'Empleados' 
        ordering = ['paterno','materno','nombre']
        unique_together= ('curp',)
        db_table = 'Empleado'

    def __str__(self):
        return '%s %s, %s' % (self.paterno, self.materno, self.nomrbe)

class Generales(models.Model,PermissionRequiredMixin):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    domicilio = models.JSONField()
    beneficiario = models.JSONField(null=True, blank=True)
    estudio = models.JSONField(null=True, blank=True)
    esperincia = models.JSONField(null=True, blank=True)
    familia = models.JSONField(null=True, blank=True)
    idioma = models.JSONField(null=True, blank=True)
    referencia = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'General' 
        verbose_name_plural = 'Generales' 
        db_table = 'Generales'

    def __str__(self):
        return '%s %s, %s' % (self.empleado.paterno, self.empleado.materno, self.empleado.nomrbe, self.domicilio)

