from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse
import json

@api_view(['POST','GET','PULL','PUT','PATCH','DELETE'])
def ruta(request):
    # Guardado de la información que llega tanto el meodo como la información
    #    bitacora = bitacora(descripcion = json.dumps(request.data)[0:254])
    #    bitacora.save()

    if request.method == 'POST' and request.data:
        datos = request.data
        if datos['empleado'] and datos['registro'] and datos['latitud'] \
            and datos['longitud']:
            empleado = datos['empleado']
            registro = datos['registro']
            latitud = datos['latitud']
            longitud = datos['longitud']
            # Guardar información
            seguimiento = Seguimiento.objects.create(
                empleado_id=empleado,
                registro=registro,
                latitud=latitud,
                longitud=longitud,
            )
            # Guardar seguimiento
            seguimiento.save()
            respuesta = {"Respuesta":"ok",}
            return Response(respuesta)
        else:
            # Se envia el mensaje de error, no envian nada
            respuesta = {"Respuesta":"No Ok",}
            return Response(respuesta)
    else:
        # Se envia el mensaje de error, no envian nada
        respuesta = {"Respuesta":"No Ok",}
        return Response(respuesta)
                
