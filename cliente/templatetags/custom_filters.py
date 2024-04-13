from django import template
from core.contantes import TIPO_PERSONA, ESTATUS_BAJA_ACTIVO
import re

register = template.Library()

@register.filter
def valor_persona(value):
    return dict(TIPO_PERSONA)[value]

@register.filter
def valor_estatus_cliente(value):
    return dict(ESTATUS_BAJA_ACTIVO)[value]
