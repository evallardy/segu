from django.shortcuts import render
from django.http import HttpResponseRedirect
from geopy.geocoders import Nominatim
import folium
from pprint import pprint
from django.views.generic import CreateView, View, TemplateView
from django.urls import reverse_lazy
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from opencage.geocoder import OpenCageGeocode
from django.db.models import Max

key = 'AIzaSyDiINE6mhkSLyeZITHQEwtOkemgtmTWYuo'

from rh.models import Empleado
from seguimiento.models import Seguimiento

class LocalizacionLugar(TemplateView):
    template_name = 'localizacion/busca_lugar.html'

    def get(self, request, *args, **kwargs):
        ultimos_registros_por_usuario = self.obtener_ultimos_registros_por_usuario()
        coordenadas = self.obtener_coordenadas(ultimos_registros_por_usuario)
        return render(request, self.template_name, {'coordenadas': coordenadas, "key": key})

    def obtener_ultimos_registros_por_usuario(self, ultimos_registros=None):
        if ultimos_registros is None:
            ultimos_registros = Seguimiento.objects.values('empleado').annotate(ultimo_registro=Max('registro'))

        ultimos_registros_por_usuario = Seguimiento.objects.filter(
            empleado__in=[registro['empleado'] for registro in ultimos_registros],
            registro__in=[registro['ultimo_registro'] for registro in ultimos_registros]
        )
        return ultimos_registros_por_usuario

    def obtener_coordenadas(self, registros):
        coordenadas = []
        for registro in registros:
            if registro.latitud and registro.longitud:
                nombre_empleado = registro.empleado
                coordenadas.append({
                    'latitud': float(registro.latitud),
                    'longitud': float(registro.longitud),
                    'nombre': nombre_empleado
                })
        return coordenadas
            
