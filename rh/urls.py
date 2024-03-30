from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_empleados, name='listar_empleados'),
    path('crear/', crear_empleado, name='crear_empleado'),
    path('modificar/<int:pk>/', modificar_empleado, name='modificar_empleado'),
    path('eliminar/<int:pk>/', confirmar_eliminar, name='confirmar_eliminar'),
    path('eliminar/<int:pk>/ok/', eliminar_empleado, name='eliminar_empleado'),
    path('consulta/<int:pk>/', consulta_empleado, name='consulta_empleado'),
]