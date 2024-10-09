from django.urls import path
from .api import ruta

urlpatterns = [
    path('', ruta, name = 'ruta'),
]