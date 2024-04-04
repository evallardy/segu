from django.urls import path
from .views import *

urlpatterns = [
    path('', ListarEmpleadosView.as_view(), name='listar_empleados'),
    path('crear/', CrearEmpleadoView.as_view(), name='crear_empleado'),
    path('modificar/<int:pk>/', ModificarEmpleadoView.as_view(), name='modificar_empleado'),
    path('eliminar/<int:pk>/', confirmar_eliminar, name='confirmar_eliminar'),
    path('eliminar/<int:pk>/ok/', eliminar_empleado, name='eliminar_empleado'),
    path('consulta/<int:pk>/', consulta_empleado, name='consulta_empleado'),
    path('domicilio/<int:pk>/', Domicilio_empleado.as_view(), name='domicilio_empleado'),
    path('beneficiario/<int:pk>/', Beneficiario_empleado.as_view(), name='beneficiario_empleado'),
    path('escolaridad/<int:pk>/', Escolaridad_empleado.as_view(), name='escolaridad_empleado'),
    path('experiencia/<int:pk>/', Experiencia_empleado.as_view(), name='experiencia_empleado'),
    path('familia/<int:pk>/', Familia_empleado.as_view(), name='familia_empleado'),
    path('idioma/<int:pk>/', Idioma_empleado.as_view(), name='idioma_empleado'),
    path('referencia/<int:pk>/', Referencia_empleado.as_view(), name='referencia_empleado'),
]