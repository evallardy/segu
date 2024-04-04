from django.urls import path
from .views import VehiculoListView, VehiculoCreateView, VehiculoDetailView, VehiculoUpdateView, VehiculoBajaView

urlpatterns = [
    path('vehiculos/', VehiculoListView.as_view(), name='vehiculo_list'),
    path('vehiculos/crear/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculos/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('vehiculos/<int:pk>/actualizar/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculos_baja/<int:pk>/', VehiculoBajaView.as_view(), name='vehiculo_baja'),
]
