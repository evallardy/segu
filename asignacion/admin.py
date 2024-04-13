from django.contrib import admin

from armamento.models import *
from asignacion.models import *
from cliente.models import *
# from contabilidad.models import *
# from core.models import *
from rh.models import *
from usuario.models import *


admin.site.register(Armamento)
admin.site.register(Asignacion)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Generales)
admin.site.register(Usuario)
admin.site.register(Vehiculo)
